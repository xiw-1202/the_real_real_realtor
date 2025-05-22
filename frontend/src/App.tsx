import React, { useState, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import ChatInterface from './components/ChatInterface';
import Header from './components/Header';
import WelcomeScreen from './components/WelcomeScreen';
import { ChatMessage, Language } from './types';
import { chatApi } from './services/api';

function App() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [currentLanguage, setCurrentLanguage] = useState<Language>('en');
  const [sessionId] = useState<string>(() => uuidv4());
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showWelcome, setShowWelcome] = useState(true);
  const [systemReady, setSystemReady] = useState(false);

  // Check system health on mount
  useEffect(() => {
    const checkSystemHealth = async () => {
      try {
        const health = await chatApi.getHealth();
        setSystemReady(health.chatbot_ready);
      } catch (error) {
        console.error('System health check failed:', error);
        setSystemReady(false);
      }
    };

    checkSystemHealth();
  }, []);

  const sendMessage = async (messageText: string) => {
    if (!messageText.trim() || isLoading) return;

    setIsLoading(true);
    setError(null);

    // Add user message
    const userMessage: ChatMessage = {
      id: uuidv4(),
      message: messageText,
      language: currentLanguage,
      session_id: sessionId,
      timestamp: new Date(),
      role: 'user'
    };

    setMessages(prev => [...prev, userMessage]);

    try {
      // Send to API
      const response = await chatApi.sendMessage({
        message: messageText,
        language: currentLanguage,
        session_id: sessionId,
        message_type: 'query'
      });

      // Add bot response with both language versions if available
      const botMessage: ChatMessage = {
        id: uuidv4(),
        message: response.message,
        message_en: response.language === 'en' ? response.message : undefined,
        message_zh: response.language === 'zh' ? response.message : undefined,
        language: response.language,
        session_id: response.session_id,
        timestamp: new Date(response.timestamp),
        role: 'assistant'
      };

      setMessages(prev => [...prev, botMessage]);

      // Hide welcome screen after first interaction
      if (showWelcome) {
        setShowWelcome(false);
      }

    } catch (error) {
      setError(error instanceof Error ? error.message : 'An error occurred');
      console.error('Error sending message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const setLanguage = (language: Language) => {
    setCurrentLanguage(language);
  };

  const clearMessages = () => {
    setMessages([]);
    setShowWelcome(true);
    setError(null);
  };

  const handleStartChat = () => {
    setShowWelcome(false);
  };

  const handleGoBack = () => {
    setShowWelcome(true);
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      <Header 
        currentLanguage={currentLanguage}
        onLanguageChange={setLanguage}
        onClearChat={clearMessages}
        systemReady={systemReady}
      />
      
      <main className="flex-1 flex flex-col overflow-hidden">
        {showWelcome ? (
          <WelcomeScreen 
            currentLanguage={currentLanguage}
            onStartChat={handleStartChat}
            onSendMessage={sendMessage}
          />
        ) : (
          <ChatInterface
            messages={messages}
            currentLanguage={currentLanguage}
            isLoading={isLoading}
            error={error}
            onSendMessage={sendMessage}
            onRetry={() => setError(null)}
            onGoBack={handleGoBack}
          />
        )}
      </main>
    </div>
  );
}

export default App;
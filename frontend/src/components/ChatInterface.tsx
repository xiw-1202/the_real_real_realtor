import React, { useState, useRef, useEffect } from 'react';
import { Send, AlertCircle, RefreshCw, ArrowLeft } from 'lucide-react';
import MessageBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';
import { ChatMessage, Language } from '../types';

interface ChatInterfaceProps {
  messages: ChatMessage[];
  currentLanguage: Language;
  isLoading: boolean;
  error: string | null;
  onSendMessage: (message: string) => void;
  onRetry: () => void;
  onGoBack: () => void;
}

const ChatInterface: React.FC<ChatInterfaceProps> = ({
  messages,
  currentLanguage,
  isLoading,
  error,
  onSendMessage,
  onRetry,
  onGoBack
}) => {
  const [inputValue, setInputValue] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const placeholders = {
    en: 'Ask me anything about renting in NYC...',
    zh: '询问关于纽约租房的任何问题...'
  };

  const sendButtonText = {
    en: 'Send',
    zh: '发送'
  };

  const errorMessages = {
    en: {
      title: 'Something went wrong',
      retry: 'Try Again'
    },
    zh: {
      title: '出现错误',
      retry: '重试'
    }
  };

  const goBackText = {
    en: 'Back to Welcome',
    zh: '返回欢迎页'
  };

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  // Focus input on mount
  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      onSendMessage(inputValue.trim());
      setInputValue('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Go Back Button */}
      <div className="px-4 py-3 border-b border-gray-200 bg-white">
        <button
          onClick={onGoBack}
          className="flex items-center space-x-2 text-gray-600 hover:text-gray-800 transition-colors duration-200"
        >
          <ArrowLeft className="h-4 w-4" />
          <span className="text-sm font-medium">{goBackText[currentLanguage]}</span>
        </button>
      </div>

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4">
        {messages.length === 0 && !isLoading && (
          <div className="text-center text-gray-500 py-8">
            <p>
              {currentLanguage === 'en' 
                ? 'Start by asking a question about renting in NYC!'
                : '开始询问关于纽约租房的问题吧！'
              }
            </p>
          </div>
        )}

        {messages.map((message) => (
          <MessageBubble
            key={message.id}
            message={message}
            currentLanguage={currentLanguage}
          />
        ))}

        {isLoading && <TypingIndicator currentLanguage={currentLanguage} />}

        {error && (
          <div className="max-w-md mx-auto bg-red-50 border border-red-200 rounded-lg p-4">
            <div className="flex items-center space-x-3">
              <AlertCircle className="h-5 w-5 text-red-500 flex-shrink-0" />
              <div className="flex-1">
                <h4 className="text-sm font-medium text-red-800">
                  {errorMessages[currentLanguage].title}
                </h4>
                <p className="text-sm text-red-600 mt-1">{error}</p>
              </div>
              <button
                onClick={onRetry}
                className="flex items-center space-x-1 text-sm text-red-600 hover:text-red-800"
              >
                <RefreshCw className="h-4 w-4" />
                <span>{errorMessages[currentLanguage].retry}</span>
              </button>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="border-t border-gray-200 bg-white px-4 py-4">
        <form onSubmit={handleSubmit} className="flex space-x-3">
          <div className="flex-1">
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder={placeholders[currentLanguage]}
              disabled={isLoading}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent disabled:bg-gray-100 disabled:cursor-not-allowed"
            />
          </div>
          <button
            type="submit"
            disabled={!inputValue.trim() || isLoading}
            className="bg-blue-500 hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition-colors duration-200 flex items-center space-x-2"
          >
            <Send className="h-4 w-4" />
            <span className="hidden sm:inline">{sendButtonText[currentLanguage]}</span>
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatInterface;
import React from 'react';
import { Bot, User, Languages } from 'lucide-react';
import { ChatMessage, Language } from '../types';
import { TranslationService } from '../services/translation';

interface MessageBubbleProps {
  message: ChatMessage;
  currentLanguage: Language;
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message, currentLanguage }) => {
  const isUser = message.role === 'user';
  
  const formatTime = (date: Date) => {
    return date.toLocaleTimeString(currentLanguage === 'zh' ? 'zh-CN' : 'en-US', {
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  // Get the display message in the current language
  const displayMessage = TranslationService.getDisplayMessage(message, currentLanguage);
  
  // Check if this message is being shown in a different language than it was sent
  const isTranslated = message.language !== currentLanguage;

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} animate-slide-up`}>
      <div className={`flex items-start space-x-3 max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg ${isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
        {/* Avatar */}
        <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
          isUser ? 'bg-blue-500' : 'bg-gray-200'
        }`}>
          {isUser ? (
            <User className="h-4 w-4 text-white" />
          ) : (
            <Bot className="h-4 w-4 text-gray-600" />
          )}
        </div>

        {/* Message Content */}
        <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'}`}>
          <div className={`chat-bubble ${isUser ? 'chat-bubble-user' : 'chat-bubble-bot'}`}>
            <p className="text-sm leading-relaxed whitespace-pre-wrap">
              {displayMessage}
            </p>
            {/* Translation indicator */}
            {isTranslated && (
              <div className="translation-indicator flex items-center space-x-1">
                <Languages className="h-3 w-3" />
                <span className="text-xs">
                  {currentLanguage === 'zh' ? '翻译' : 'Translated'}
                </span>
              </div>
            )}
          </div>
          
          {/* Timestamp */}
          <span className="text-xs text-gray-400 mt-1 px-2">
            {formatTime(message.timestamp)}
          </span>
        </div>
      </div>
    </div>
  );
};

export default MessageBubble;
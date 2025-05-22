import React from 'react';
import { Bot } from 'lucide-react';
import { Language } from '../types';

interface TypingIndicatorProps {
  currentLanguage: Language;
}

const TypingIndicator: React.FC<TypingIndicatorProps> = ({ currentLanguage }) => {
  const typingText = {
    en: 'Assistant is typing...',
    zh: '助手正在输入...'
  };

  return (
    <div className="flex justify-start animate-fade-in">
      <div className="flex items-start space-x-3 max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg">
        {/* Avatar */}
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center">
          <Bot className="h-4 w-4 text-gray-600" />
        </div>

        {/* Typing Indicator */}
        <div className="chat-bubble chat-bubble-bot">
          <div className="flex items-center space-x-2">
            <span className="text-sm text-gray-600">{typingText[currentLanguage]}</span>
            <div className="flex space-x-1">
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-pulse"></div>
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-pulse" style={{ animationDelay: '0.1s' }}></div>
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-pulse" style={{ animationDelay: '0.2s' }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TypingIndicator;
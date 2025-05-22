import React from 'react';
import { Home, Trash2 } from 'lucide-react';
import { Language } from '../types';

interface HeaderProps {
  currentLanguage: Language;
  onLanguageChange: (language: Language) => void;
  onClearChat: () => void;
  systemReady: boolean;
}

const Header: React.FC<HeaderProps> = ({
  currentLanguage,
  onLanguageChange,
  onClearChat,
  systemReady
}) => {
  const titles = {
    en: 'The Real Real Realtor',
    zh: '真正的房地产经纪人'
  };

  const clearButtonText = {
    en: 'Clear Chat',
    zh: '清除对话'
  };

  return (
    <header className="bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <div className="flex items-center space-x-2">
          <Home className="h-6 w-6 text-blue-500" />
          <h1 className="text-xl font-semibold text-gray-900">
            {titles[currentLanguage]}
          </h1>
        </div>
        
        {/* System Status Indicator */}
        <div className="flex items-center space-x-2">
          <div className={`w-2 h-2 rounded-full ${systemReady ? 'bg-green-500' : 'bg-red-500'}`} />
          <span className="text-xs text-gray-500">
            {systemReady ? (currentLanguage === 'en' ? 'Online' : '在线') : (currentLanguage === 'en' ? 'Offline' : '离线')}
          </span>
        </div>
      </div>

      <div className="flex items-center space-x-3">
        {/* Language Toggle */}
        <div className="flex items-center space-x-1 bg-gray-100 rounded-full p-1">
          <button
            onClick={() => onLanguageChange('en')}
            className={`language-toggle ${currentLanguage === 'en' ? 'active' : ''}`}
          >
            EN
          </button>
          <button
            onClick={() => onLanguageChange('zh')}
            className={`language-toggle ${currentLanguage === 'zh' ? 'active' : ''}`}
          >
            中文
          </button>
        </div>

        {/* Clear Chat Button */}
        <button
          onClick={onClearChat}
          className="flex items-center space-x-2 px-3 py-2 text-sm text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors duration-200"
        >
          <Trash2 className="h-4 w-4" />
          <span className="hidden sm:inline">{clearButtonText[currentLanguage]}</span>
        </button>
      </div>
    </header>
  );
};

export default Header;
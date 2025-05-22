/**
 * Simple Translation Service for The Real Real Realtor
 * 真正的房地产经纪人简单翻译服务
 */

import { ChatMessage } from '../types';

// Common rental-related translations
const commonTranslations: Record<string, { en: string; zh: string }> = {
  // Greetings
  'hello': { en: 'Hello', zh: '你好' },
  'hi': { en: 'Hi', zh: '嗨' },
  'thank you': { en: 'Thank you', zh: '谢谢' },
  'thanks': { en: 'Thanks', zh: '谢谢' },
  
  // Common questions
  'what documents do i need to rent an apartment': {
    en: 'What documents do I need to rent an apartment?',
    zh: '租房需要什么文件？'
  },
  'how do i find apartments near nyu': {
    en: 'How do I find apartments near NYU?',
    zh: '如何找到纽约大学附近的公寓？'
  },
  'what\'s the difference between manhattan and jersey city': {
    en: 'What\'s the difference between Manhattan and Jersey City?',
    zh: '曼哈顿和泽西市有什么区别？'
  },
  'how do i set up utilities': {
    en: 'How do I set up utilities?',
    zh: '如何设置水电煤气？'
  },
  
  // Common responses
  'i can help you with': {
    en: 'I can help you with',
    zh: '我可以帮助您'
  },
  'to rent an apartment in nyc': {
    en: 'To rent an apartment in NYC',
    zh: '在纽约租房'
  },
  'you typically need': {
    en: 'you typically need',
    zh: '您通常需要'
  }
};

export class TranslationService {
  /**
   * Attempt to translate a message using common translations
   */
  static translateMessage(message: string, targetLanguage: 'en' | 'zh'): string {
    const messageLower = message.toLowerCase().trim();
    
    // Check for exact matches first
    if (commonTranslations[messageLower]) {
      return commonTranslations[messageLower][targetLanguage];
    }
    
    // Check for partial matches
    for (const [key, translation] of Object.entries(commonTranslations)) {
      if (messageLower.includes(key) || key.includes(messageLower)) {
        return translation[targetLanguage];
      }
    }
    
    // If no translation found, return original message with a note
    const noTranslationNote = {
      en: message, // Keep original if it's already English
      zh: message  // Keep original if it's already Chinese
    };
    
    return noTranslationNote[targetLanguage];
  }
  
  /**
   * Get the display message based on current language
   */
  static getDisplayMessage(
    message: ChatMessage, 
    currentLanguage: 'en' | 'zh'
  ): string {
    // If we have a translation in the target language, use it
    if (currentLanguage === 'zh' && message.message_zh) {
      return message.message_zh;
    }
    if (currentLanguage === 'en' && message.message_en) {
      return message.message_en;
    }
    
    // If the message is already in the target language, return as is
    if (message.language === currentLanguage) {
      return message.message;
    }
    
    // Try to translate using our simple translation service
    return this.translateMessage(message.message, currentLanguage);
  }
  
  /**
   * Check if a message can be translated
   */
  static canTranslate(message: string): boolean {
    const messageLower = message.toLowerCase().trim();
    return Object.keys(commonTranslations).some(key => 
      messageLower.includes(key) || key.includes(messageLower)
    );
  }
}

export default TranslationService;
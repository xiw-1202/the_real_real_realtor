export interface ChatMessage {
  id: string;
  message: string;
  message_zh?: string; // Chinese translation
  message_en?: string; // English translation
  language: 'en' | 'zh';
  session_id?: string;
  message_type?: 'query' | 'greeting' | 'feedback' | 'clarification';
  context?: Record<string, any>;
  timestamp: Date;
  role: 'user' | 'assistant';
}

export interface Source {
  title: string;
  title_zh?: string;
  content_snippet: string;
  relevance_score: number;
  document_type: string;
  topic: string;
}

export interface Suggestion {
  text: string;
  text_zh?: string;
  intent: string;
  confidence: number;
}

export interface ChatResponse {
  message: string;
  language: 'en' | 'zh';
  confidence: number;
  sources: Source[];
  suggestions: Suggestion[];
  session_id?: string;
  response_time_ms?: number;
  timestamp: Date;
}

export interface ApiChatMessage {
  message: string;
  language: 'en' | 'zh';
  session_id?: string;
  message_type?: 'query' | 'greeting' | 'feedback' | 'clarification';
  context?: Record<string, any>;
}

export interface ApiChatResponse {
  message: string;
  language: 'en' | 'zh';
  confidence: number;
  sources: Source[];
  suggestions: Suggestion[];
  session_id?: string;
  response_time_ms?: number;
  timestamp: string;
}

export interface TopicCategory {
  name: string;
  name_zh: string;
  description: string;
  description_zh: string;
  entry_count: number;
  keywords: string[];
}

export interface SystemHealth {
  status: string;
  timestamp: string;
  version: string;
  chatbot_ready: boolean;
}

export type Language = 'en' | 'zh';

export interface ChatContextType {
  messages: ChatMessage[];
  currentLanguage: Language;
  sessionId: string;
  isLoading: boolean;
  error: string | null;
  sendMessage: (message: string) => Promise<void>;
  setLanguage: (language: Language) => void;
  clearMessages: () => void;
}
import axios from 'axios';
import { ApiChatMessage, ApiChatResponse, TopicCategory, SystemHealth } from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to ${config.url}`);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    console.log(`Response from ${response.config.url}:`, response.status);
    return response;
  },
  (error) => {
    console.error('Response error:', error);
    
    if (error.response) {
      console.error('Error response:', error.response.data);
    } else if (error.request) {
      console.error('No response received:', error.request);
    }
    
    return Promise.reject(error);
  }
);

export const chatApi = {
  // Send chat message
  sendMessage: async (message: ApiChatMessage): Promise<ApiChatResponse> => {
    try {
      const response = await api.post<ApiChatResponse>('/chat', message);
      return response.data;
    } catch (error) {
      console.error('Error sending chat message:', error);
      throw new Error('Failed to send message. Please try again.');
    }
  },

  // Get available topics
  getTopics: async (): Promise<TopicCategory[]> => {
    try {
      const response = await api.get<TopicCategory[]>('/topics');
      return response.data;
    } catch (error) {
      console.error('Error fetching topics:', error);
      throw new Error('Failed to fetch topics');
    }
  },

  // Submit feedback
  submitFeedback: async (feedback: {
    session_id: string;
    message_id?: string;
    rating: number;
    feedback_text?: string;
    feedback_type: string;
  }): Promise<{ status: string; message: string }> => {
    try {
      const response = await api.post('/feedback', feedback);
      return response.data;
    } catch (error) {
      console.error('Error submitting feedback:', error);
      throw new Error('Failed to submit feedback');
    }
  },

  // Get system health
  getHealth: async (): Promise<SystemHealth> => {
    try {
      const response = await api.get<SystemHealth>('/health');
      return response.data;
    } catch (error) {
      console.error('Error checking system health:', error);
      throw new Error('Failed to check system health');
    }
  },

  // Get system statistics
  getStats: async (): Promise<any> => {
    try {
      const response = await api.get('/stats');
      return response.data;
    } catch (error) {
      console.error('Error fetching stats:', error);
      throw new Error('Failed to fetch statistics');
    }
  }
};

export default api;
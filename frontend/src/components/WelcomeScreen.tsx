import React from 'react';
import { MessageCircle, Home, MapPin, FileText, DollarSign } from 'lucide-react';
import { Language } from '../types';

interface WelcomeScreenProps {
  currentLanguage: Language;
  onStartChat: () => void;
  onSendMessage: (message: string) => void;
}

const WelcomeScreen: React.FC<WelcomeScreenProps> = ({
  currentLanguage,
  onStartChat,
  onSendMessage
}) => {
  const content = {
    en: {
      title: 'Welcome to The Real Real Realtor',
      subtitle: 'Your trusted bilingual guide to finding apartments in Manhattan and Jersey City',
      description: 'I can help Chinese international students with:',
      features: [
        { icon: Home, text: 'Finding apartments near your university' },
        { icon: FileText, text: 'Understanding lease documents and application process' },
        { icon: DollarSign, text: 'Setting up utilities and banking' },
        { icon: MapPin, text: 'Neighborhood recommendations and safety tips' }
      ],
      universities: 'Supporting students from NYU, Columbia, FIT, The New School, SVA, Fordham, and Stevens',
      quickStart: 'Quick Start Questions:',
      startButton: 'Start Chatting',
      sampleQuestions: [
        'What documents do I need to rent an apartment?',
        'How do I find apartments near NYU?',
        'What\'s the difference between Manhattan and Jersey City?',
        'How do I set up utilities in my new apartment?'
      ]
    },
    zh: {
      title: '欢迎使用真正的房地产经纪人',
      subtitle: '为您提供曼哈顿和泽西市找房的可信双语指导',
      description: '我可以帮助中国留学生解决：',
      features: [
        { icon: Home, text: '在大学附近找公寓' },
        { icon: FileText, text: '理解租约文件和申请流程' },
        { icon: DollarSign, text: '设置水电煤气和银行业务' },
        { icon: MapPin, text: '社区推荐和安全建议' }
      ],
      universities: '为NYU、哥伦比亚、FIT、新学院、SVA、福德汉姆和史蒂文斯的学生提供支持',
      quickStart: '快速开始问题：',
      startButton: '开始聊天',
      sampleQuestions: [
        '租房需要什么文件？',
        '如何找到纽约大学附近的公寓？',
        '曼哈顿和泽西市有什么区别？',
        '如何在新公寓设置水电煤气？'
      ]
    }
  };

  const currentContent = content[currentLanguage];

  const handleQuestionClick = (question: string) => {
    onSendMessage(question);
  };

  return (
    <div className="flex-1 flex items-center justify-center p-4">
      <div className="max-w-4xl w-full">
        <div className="text-center mb-8">
          <div className="mb-6">
            <div className="mx-auto w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center mb-4">
              <MessageCircle className="h-8 w-8 text-white" />
            </div>
            <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-2">
              {currentContent.title}
            </h1>
            <p className="text-lg text-gray-600 mb-4">
              {currentContent.subtitle}
            </p>
            <p className="text-sm text-gray-500">
              {currentContent.universities}
            </p>
          </div>
        </div>

        <div className="grid md:grid-cols-2 gap-8 mb-8">
          {/* Features */}
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">
              {currentContent.description}
            </h3>
            <div className="space-y-3">
              {currentContent.features.map((feature, index) => (
                <div key={index} className="flex items-center space-x-3">
                  <feature.icon className="h-5 w-5 text-blue-500 flex-shrink-0" />
                  <span className="text-gray-700">{feature.text}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Quick Start Questions */}
          <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">
              {currentContent.quickStart}
            </h3>
            <div className="space-y-2">
              {currentContent.sampleQuestions.map((question, index) => (
                <button
                  key={index}
                  onClick={() => handleQuestionClick(question)}
                  className="w-full text-left p-3 rounded-lg border border-gray-200 hover:border-blue-300 hover:bg-blue-50 transition-colors duration-200 text-sm text-gray-700 hover:text-blue-700"
                >
                  {question}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Start Button */}
        <div className="text-center">
          <button
            onClick={onStartChat}
            className="bg-blue-500 hover:bg-blue-600 text-white px-8 py-3 rounded-lg font-medium transition-colors duration-200 shadow-sm"
          >
            {currentContent.startButton}
          </button>
        </div>
      </div>
    </div>
  );
};

export default WelcomeScreen;
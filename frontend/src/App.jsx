import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import TheoryColumn from './components/TheoryColumn';
import PracticeColumn from './components/PracticeColumn';
import confetti from 'canvas-confetti';

export default function App() {
  const [currentWeekId, setCurrentWeekId] = useState('week1_intro');
  const [theory, setTheory] = useState('');
  const [initialCode, setInitialCode] = useState('');
  const [sampleCode, setSampleCode] = useState('');
  const [completedWeeks, setCompletedWeeks] = useState(() => {
    const saved = localStorage.getItem('python_completed_weeks');
    return saved ? JSON.parse(saved) : [];
  });

  // Tải nội dung bài học & code mẫu khi đổi tuần học
  useEffect(() => {
    // Đặt lại state hiển thị loading
    setTheory('');
    
    // Tải file lý thuyết README.md
    fetch(`/lessons/${currentWeekId}/README.md`)
      .then((res) => {
        if (!res.ok) {
          throw new Error('Không thể tải bài giảng');
        }
        return res.text();
      })
      .then((text) => setTheory(text))
      .catch((err) => {
        console.error(err);
        setTheory('# Lỗi tải bài học 😢\nKhông thể kết nối đến máy chủ bài học. Vui lòng thử lại!');
      });

    // Tải file code mẫu project.py
    fetch(`/lessons/${currentWeekId}/project.py`)
      .then((res) => {
        if (!res.ok) {
          throw new Error('Không thể tải code mẫu');
        }
        return res.text();
      })
      .then((text) => {
        setInitialCode(text);
        setSampleCode(text);
      })
      .catch((err) => {
        console.error(err);
        setInitialCode('# Hic! Lỗi tải code mẫu rồi.');
      });
  }, [currentWeekId]);

  // Callback kích hoạt khi chạy code Python thành công
  const handleRunSuccess = () => {
    // Bắn pháo hoa giấy chúc mừng bé!
    confetti({
      particleCount: 150,
      spread: 85,
      origin: { y: 0.6 },
      colors: ['#58cc02', '#1cb0f6', '#ff9600', '#854eee', '#ff4b4b', '#ffc800']
    });

    // Cập nhật trạng thái hoàn thành
    if (!completedWeeks.includes(currentWeekId)) {
      const updated = [...completedWeeks, currentWeekId];
      setCompletedWeeks(updated);
      localStorage.setItem('python_completed_weeks', JSON.stringify(updated));
    }
  };

  return (
    <div className="app-container">
      {/* Sidebar chọn tuần học */}
      <Sidebar
        currentWeekId={currentWeekId}
        onSelectWeek={setCurrentWeekId}
        completedWeeks={completedWeeks}
      />

      {/* Nội dung chính chia 2 cột */}
      <main className="main-content">
        {/* Cột trái: Lý thuyết */}
        <TheoryColumn markdownContent={theory} />

        {/* Cột phải: Thực hành */}
        <PracticeColumn
          currentWeekId={currentWeekId}
          initialCode={initialCode}
          sampleCode={sampleCode}
          onRunSuccess={handleRunSuccess}
        />
      </main>
    </div>
  );
}

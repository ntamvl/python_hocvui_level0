import React from 'react';
import { BookOpen, CheckCircle, Award } from 'lucide-react';

const weeks = [
  { id: 'week1_intro', title: 'Tuần 1: Chào bạn Python! 🐍', desc: 'Làm quen & Lệnh Print' },
  { id: 'week2_variables', title: 'Tuần 2: Hộp đồ chơi 📦', desc: 'Biến & Phép toán cơ bản' },
  { id: 'week3_conditions', title: 'Tuần 3: Gương thần 🔮', desc: 'Điều kiện If - Else' },
  { id: 'week4_loops', title: 'Tuần 4: Hỏa tiễn bay 🚀', desc: 'Vòng lặp For & While' },
  { id: 'week5_functions', title: 'Tuần 5: Máy ma thuật 🍞', desc: 'Học cách tạo Hàm' },
  { id: 'week6_classes', title: 'Tuần 6: Quái thú ảo 👾', desc: 'Lớp & Đối tượng' }
];

export default function Sidebar({ currentWeekId, onSelectWeek, completedWeeks }) {
  return (
    <aside className="kids-sidebar">
      <div className="sidebar-header">
        <h1 className="sidebar-title">Python Học Vui 🐍</h1>
        <div className="sidebar-subtitle">Lập trình cho Siêu Nhí (12+)</div>
      </div>
      
      <div className="lessons-list">
        {weeks.map((week, index) => {
          const isActive = week.id === currentWeekId;
          const isCompleted = completedWeeks.includes(week.id);
          
          return (
            <div
              key={week.id}
              className={`lesson-item ${isActive ? 'active' : ''}`}
              onClick={() => onSelectWeek(week.id)}
            >
              <div className="lesson-number">
                {isCompleted ? (
                  <CheckCircle size={20} className="text-white" style={{ fill: 'var(--color-green)' }} />
                ) : (
                  index + 1
                )}
              </div>
              <div className="flex-grow-1">
                <div style={{ fontSize: '0.95rem', marginBottom: '2px' }}>{week.title}</div>
                <div style={{ fontSize: '0.75rem', color: isActive ? '#1cb0f6' : '#888', fontWeight: '500' }}>
                  {week.desc}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="p-3 border-top text-center" style={{ backgroundColor: '#fafafa', borderRadius: '0 0 0 16px' }}>
        <div className="d-flex align-items-center justify-content-center gap-2" style={{ fontWeight: 800, color: 'var(--color-purple)' }}>
          <Award size={22} />
          <span>Hoàn thành: {completedWeeks.length} / 6</span>
        </div>
      </div>
    </aside>
  );
}

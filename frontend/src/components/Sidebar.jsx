import React, { useState, useEffect } from 'react';
import { CheckCircle, Award } from 'lucide-react';

const levels = [
  {
    id: 'level1',
    title: 'Cấp 1: Căn Bản 🚀',
    subtitle: 'Nền tảng Python',
    weeks: [
      { id: 'level1/week1_intro', title: 'Tuần 1: Chào bạn Python!', desc: 'Làm quen & Lệnh Print' },
      { id: 'level1/week2_variables', title: 'Tuần 2: Hộp đồ chơi 📦', desc: 'Biến & Phép toán cơ bản' },
      { id: 'level1/week3_conditions', title: 'Tuần 3: Gương thần 🔮', desc: 'Điều kiện If - Else' },
      { id: 'level1/week4_loops', title: 'Tuần 4: Hỏa tiễn bay 🚀', desc: 'Vòng lặp For & While' },
      { id: 'level1/week5_functions', title: 'Tuần 5: Máy ma thuật 🍞', desc: 'Học cách tạo Hàm' },
      { id: 'level1/week6_classes', title: 'Tuần 6: Quái thú ảo 👾', desc: 'Lớp & Đối tượng' }
    ]
  },
  {
    id: 'level2',
    title: 'Cấp 2: Thám Hiểm 💎',
    subtitle: 'Cấu trúc & Nâng cao',
    weeks: [
      { id: 'level2/week1_typecast_builtins', title: 'Tuần 1: Siêu công cụ 🧰', desc: 'Ép kiểu & Hàm Built-in' },
      { id: 'level2/week2_list', title: 'Tuần 2: Balo danh sách 🎒', desc: 'Cấu trúc dữ liệu List' },
      { id: 'level2/week3_tuple_set', title: 'Tuần 3: Huy hiệu & Tọa độ 🧭', desc: 'Tuple & Set độc nhất' },
      { id: 'level2/week4_dictionary', title: 'Tuần 4: Từ điển thông minh 📖', desc: 'Dictionary (Key - Value)' },
      { id: 'level2/week5_functions_advanced', title: 'Tuần 5: Xưởng nâng cấp ⚡', desc: 'Hàm nâng cao & Lambda' },
      { id: 'level2/week6_exceptions', title: 'Tuần 6: Khiên bảo vệ 🛡️', desc: 'Xử lý lỗi & Exception' }
    ]
  },
  {
    id: 'level3',
    title: 'Cấp 3: Chuyên Gia 🏆',
    subtitle: 'Thuật toán & OOP Nâng cao',
    weeks: [
      { id: 'level3/week1_recursion', title: 'Tuần 1: Búp bê Matryoshka 🪆', desc: 'Hàm Đệ quy (Recursion)' },
      { id: 'level3/week2_sorting', title: 'Tuần 2: Thợ may xếp hàng 📊', desc: 'Thuật toán Sắp xếp' },
      { id: 'level3/week3_inheritance', title: 'Tuần 3: Siêu anh hùng 🦸‍♂️', desc: 'Kế thừa trong OOP' },
      { id: 'level3/week4_methods', title: 'Tuần 4: Tuyệt chiêu Class 🛠️', desc: 'Instance, Class & Static' },
      { id: 'level3/week5_dunder', title: 'Tuần 5: Phép thuật Python 🪄', desc: 'Phương thức Dunder' },
      { id: 'level3/week6_synthesis', title: 'Tuần 6: Đấu trường Võ thuật 🏆', desc: 'Dự án Tổng hợp Level 3' }
    ]
  }
];

export default function Sidebar({ currentWeekId, onSelectWeek, completedWeeks }) {
  const levelIdFromWeek = currentWeekId.split('/')[0] || 'level1';
  const [activeLevelId, setActiveLevelId] = useState(levelIdFromWeek);

  // Tự động chuyển tab khi currentWeekId thay đổi từ bên ngoài
  useEffect(() => {
    const lvlId = currentWeekId.split('/')[0];
    if (lvlId && levels.some((l) => l.id === lvlId)) {
      setActiveLevelId(lvlId);
    }
  }, [currentWeekId]);

  const activeLevelObj = levels.find((l) => l.id === activeLevelId) || levels[0];
  const totalWeeks = levels.reduce((acc, l) => acc + l.weeks.length, 0);

  return (
    <aside className="kids-sidebar">
      <div className="sidebar-header">
        <h1 className="sidebar-title">Python Học Vui</h1>
        <div className="sidebar-subtitle">Lập trình cho Siêu Nhí (12+)</div>
      </div>

      {/* Thanh chuyển đổi Cấp độ (Level 1 / Level 2 / Level 3) */}
      <div className="level-selector">
        {levels.map((lvl) => {
          const isActive = lvl.id === activeLevelId;
          return (
            <button
              key={lvl.id}
              className={`level-tab ${isActive ? 'active' : ''}`}
              onClick={() => setActiveLevelId(lvl.id)}
            >
              {lvl.title}
            </button>
          );
        })}
      </div>

      {/* Danh sách bài học của Cấp độ đang chọn */}
      <div className="lessons-list">
        {activeLevelObj.weeks.map((week, index) => {
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

      {/* Thống kê tiến độ hoàn thành */}
      <div className="p-3 border-top text-center" style={{ backgroundColor: '#fafafa', borderRadius: '0 0 0 16px' }}>
        <div className="d-flex align-items-center justify-content-center gap-2" style={{ fontWeight: 800, color: 'var(--color-purple)' }}>
          <Award size={22} />
          <span>Hoàn thành: {completedWeeks.length} / {totalWeeks}</span>
        </div>
      </div>
    </aside>
  );
}

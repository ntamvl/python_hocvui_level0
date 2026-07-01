import React from 'react';
import ReactMarkdown from 'react-markdown';

// Hàm helper để loại bỏ các chuỗi đánh dấu cảnh báo của github như [!NOTE] khỏi hiển thị
const removeAlertPrefix = (children, ...prefixes) => {
  return React.Children.map(children, child => {
    if (child && child.props && child.props.children) {
      const innerChildren = React.Children.toArray(child.props.children);
      const modifiedInner = innerChildren.map(inner => {
        if (typeof inner === 'string') {
          let temp = inner;
          prefixes.forEach(p => {
            temp = temp.replace(p, '').trim();
          });
          return temp;
        }
        return inner;
      });
      return React.cloneElement(child, {}, ...modifiedInner);
    }
    return child;
  });
};

const CustomBlockquote = ({ children }) => {
  // Tìm kiếm xem có ký hiệu cảnh báo nào không
  let rawText = '';
  React.Children.forEach(children, child => {
    if (child && child.props && child.props.children) {
      React.Children.forEach(child.props.children, inner => {
        if (typeof inner === 'string') rawText += inner;
      });
    }
  });

  let boxClass = 'note-box';
  let title = '📝 LƯU Ý';
  let cleanChildren = children;

  if (rawText.includes('[!NOTE]')) {
    boxClass = 'note-box';
    title = '📝 Mẹo nhỏ cho bé';
    cleanChildren = removeAlertPrefix(children, '[!NOTE]');
  } else if (rawText.includes('[!TIP]')) {
    boxClass = 'tip-box';
    title = '💡 Gợi ý hay';
    cleanChildren = removeAlertPrefix(children, '[!TIP]');
  } else if (rawText.includes('[!IMPORTANT]') || rawText.includes('[!WARNING]')) {
    boxClass = 'warning-box';
    title = '⚠️ Chú ý nè';
    cleanChildren = removeAlertPrefix(children, '[!IMPORTANT]', '[!WARNING]');
  } else if (rawText.toLowerCase().includes('thử thách') || rawText.toLowerCase().includes('challenge')) {
    boxClass = 'challenge-box';
    title = '🌟 THỬ THÁCH CHO BÉ';
  }

  return (
    <div className={boxClass}>
      <h6 className="mb-2" style={{ fontWeight: 800, fontSize: '0.95rem', letterSpacing: '0.5px' }}>{title}</h6>
      <div style={{ fontSize: '0.95rem', margin: 0 }}>{cleanChildren}</div>
    </div>
  );
};

export default function TheoryColumn({ markdownContent }) {
  if (!markdownContent) {
    return (
      <div className="theory-column d-flex align-items-center justify-content-center">
        <div className="text-center text-muted">
          <div className="spinner-border text-primary mb-3" role="status"></div>
          <div>Đang mở sách bài học... 📖</div>
        </div>
      </div>
    );
  }

  return (
    <div className="theory-column markdown-body">
      <ReactMarkdown
        components={{
          blockquote: CustomBlockquote
        }}
      >
        {markdownContent}
      </ReactMarkdown>
    </div>
  );
}

import React, { useState, useEffect, useRef } from 'react';
import { Play, RotateCcw, HelpCircle, Terminal as TerminalIcon } from 'lucide-react';
import { highlightPython } from '../utils/pythonHighlighter';

export default function PracticeColumn({ currentWeekId, initialCode, sampleCode, onRunSuccess }) {
  const [code, setCode] = useState(initialCode);
  const [output, setOutput] = useState([]);
  const [isRunning, setIsRunning] = useState(false);
  const [pyodideInstance, setPyodideInstance] = useState(null);
  const [isPyodideLoading, setIsPyodideLoading] = useState(true);
  const [loadingStatus, setLoadingStatus] = useState('Đang đánh thức chú rắn Python... 🐍');
  const textareaRef = useRef(null);
  const lineNumbersRef = useRef(null);
  const highlightRef = useRef(null);

  // Khởi tạo Pyodide khi component mount
  useEffect(() => {
    async function initPyodide() {
      if (window.loadPyodide) {
        try {
          setLoadingStatus('Đang nạp bộ xử lý Python WebAssembly... ⚙️');
          const pyodide = await window.loadPyodide();
          setLoadingStatus('Đang chuẩn bị môi trường chạy thử... 🚀');
          // Chạy thử một lệnh trống để warmup
          await pyodide.runPythonAsync('print("Python Ready!")');
          setPyodideInstance(pyodide);
          setIsPyodideLoading(false);
        } catch (err) {
          console.error(err);
          setLoadingStatus('Hic! Không thể tải Python. Vui lòng làm mới trang (F5).');
        }
      } else {
        setLoadingStatus('Không tìm thấy thư viện Pyodide. Đang tải lại... 🔄');
        // Thử check lại sau 1s nếu script CDN chưa load xong
        setTimeout(initPyodide, 1000);
      }
    }
    initPyodide();
  }, []);

  // Cập nhật code khi chuyển đổi tuần học
  useEffect(() => {
    setCode(initialCode);
    setOutput([]);
  }, [currentWeekId, initialCode]);

  // Đồng bộ hóa cuộn giữa textarea, cột số dòng và phần tô màu
  const handleScroll = (e) => {
    const { scrollTop, scrollLeft } = e.target;
    if (lineNumbersRef.current) {
      lineNumbersRef.current.scrollTop = scrollTop;
    }
    if (highlightRef.current) {
      highlightRef.current.scrollTop = scrollTop;
      highlightRef.current.scrollLeft = scrollLeft;
    }
  };

  // Hỗ trợ phím Tab để viết thụt lề 4 khoảng trắng giống các IDE xịn
  const handleKeyDown = (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const { selectionStart, selectionEnd } = e.target;
      const newCode = code.substring(0, selectionStart) + '    ' + code.substring(selectionEnd);
      setCode(newCode);

      // Đặt lại con trỏ chuột ngay sau 4 dấu cách vừa chèn
      setTimeout(() => {
        if (textareaRef.current) {
          textareaRef.current.selectionStart = textareaRef.current.selectionEnd = selectionStart + 4;
        }
      }, 0);
    }
  };

  // Tính số dòng để vẽ cột line number
  const lineCount = code.split('\n').length;
  const lineNumbers = Array.from({ length: lineCount }, (_, i) => i + 1);

  // Xem code mẫu
  const handleLoadSample = () => {
    setCode(sampleCode);
    setOutput([{ text: '💡 Đã nạp code mẫu! Hãy nhấn "Bấm để Chạy thử! 🚀" để chạy.', type: 'info' }]);
  };

  // Đặt lại code ban đầu
  const handleReset = () => {
    setCode(initialCode);
    setOutput([{ text: '🔄 Đã khôi phục code ban đầu của tuần.', type: 'info' }]);
  };

  // Làm sạch lỗi Python để trẻ em dễ hiểu hơn
  const formatFriendlyError = (rawError) => {
    const errorStr = String(rawError);
    let friendlyMessage = "Hic! Hình như có một lỗi nhỏ trong code của bạn. Hãy kiểm tra lại nhé! 🧐\n\n";

    if (errorStr.includes('SyntaxError')) {
      friendlyMessage += "👉 LỖI CÚ PHÁP (SyntaxError):\nCó vẻ bạn viết thiếu dấu ngoặc (), dấu nháy \"\" hoặc dấu hai chấm : ở đâu đó rồi!";
    } else if (errorStr.includes('NameError')) {
      const match = errorStr.match(/name '(\w+)' is not defined/);
      const varName = match ? match[1] : '';
      friendlyMessage += `👉 LỖI TÊN GỌI (NameError):\nBạn đang gọi tên "${varName}" nhưng Python chưa biết chiếc hộp/biến này là gì! Bạn đã tạo nó chưa, hoặc có viết sai chính tả không?`;
    } else if (errorStr.includes('IndentationError')) {
      friendlyMessage += "👉 LỖI CĂN LỀ (IndentationError):\nCác dòng lệnh con (sau lệnh if, elif, else, while, def, class) phải được lùi lề vào trong (nhấn phím Tab hoặc 4 dấu cách) nhé!";
    } else if (errorStr.includes('TypeError')) {
      friendlyMessage += "👉 LỖI KIỂU DỮ LIỆU (TypeError):\nBạn đang cố thực hiện phép tính giữa hai thứ không hợp lệ (ví dụ: cộng Số với Chữ mà không chuyển đổi).";
    } else {
      friendlyMessage += `👉 Chi tiết lỗi từ Python:\n${errorStr.split('\n').slice(-2).join('\n')}`;
    }
    return friendlyMessage;
  };

  // Chạy code Python
  const handleRunCode = async () => {
    if (isPyodideLoading || !pyodideInstance) return;
    setIsRunning(true);
    setOutput([{ text: '⏳ Đang chạy code Python...', type: 'info' }]);

    try {
      // Chuyển hướng stdout của Python sang StringIO
      await pyodideInstance.runPythonAsync(`
import sys
import io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
`);

      // Thực thi code của người dùng
      await pyodideInstance.runPythonAsync(code);

      // Lấy giá trị stdout
      const stdout = await pyodideInstance.runPythonAsync('sys.stdout.getvalue()');
      const stderr = await pyodideInstance.runPythonAsync('sys.stderr.getvalue()');

      const outputs = [];
      if (stdout) {
        outputs.push({ text: stdout, type: 'stdout' });
      }
      if (stderr) {
        outputs.push({ text: stderr, type: 'error' });
      }

      if (outputs.length === 0) {
        outputs.push({ text: 'Code chạy thành công nhưng không in ra kết quả nào. (Hãy dùng lệnh print() để in kết quả nhé!)', type: 'empty' });
      } else if (!stderr) {
        // Chạy thành công không lỗi và có output
        outputs.push({ text: '🎉 Tuyệt vời ông mặt trời! Code đã chạy thành công mỹ mãn! 🥳', type: 'success' });
        // Bắn confetti chúc mừng!
        if (onRunSuccess) {
          onRunSuccess();
        }
      }

      setOutput(outputs);
    } catch (err) {
      setOutput([{ text: formatFriendlyError(err.message), type: 'error' }]);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="practice-column">
      <div className="practice-header">
        <h2 className="practice-title">Sân chơi lập trình của bé 🎮</h2>
        <div className="d-flex gap-2">
          <button 
            className="btn-kids btn-kids-secondary py-1 px-3 d-flex align-items-center gap-1"
            onClick={handleReset}
            disabled={isPyodideLoading}
          >
            <RotateCcw size={16} />
            <span>Đặt lại 🔄</span>
          </button>
          <button 
            className="btn-kids btn-kids-blue py-1 px-3 d-flex align-items-center gap-1"
            onClick={handleLoadSample}
            disabled={isPyodideLoading}
          >
            <HelpCircle size={16} />
            <span>Xem Code Mẫu 💡</span>
          </button>
        </div>
      </div>

      {/* Code Editor Container */}
      <div className="editor-container">
        <div className="editor-header">
          <div className="editor-dots">
            <span className="editor-dot dot-red"></span>
            <span className="editor-dot dot-yellow"></span>
            <span className="editor-dot dot-green"></span>
          </div>
          <span className="editor-lang">project.py</span>
        </div>
        
        <div className="editor-textarea-wrapper">
          {/* Màn hình loading Pyodide */}
          {isPyodideLoading && (
            <div className="pyodide-loading-overlay">
              <div className="loader-spinner"></div>
              <div className="loader-text">{loadingStatus}</div>
            </div>
          )}

          <div className="line-numbers" ref={lineNumbersRef}>
            {lineNumbers.map(n => (
              <div key={n}>{n}</div>
            ))}
          </div>
          
          <div className="editor-input-area">
            <pre className="code-highlight" ref={highlightRef} aria-hidden="true">
              <code dangerouslySetInnerHTML={{ __html: highlightPython(code) + '\n' }} />
            </pre>
            <textarea
              ref={textareaRef}
              className="code-textarea"
              value={code}
              onChange={(e) => setCode(e.target.value)}
              onScroll={handleScroll}
              onKeyDown={handleKeyDown}
              placeholder="# Hãy viết code Python của bạn ở đây..."
              spellCheck="false"
            />
          </div>
        </div>
      </div>

      {/* Button Run Code khổng lồ */}
      <div className="text-center mb-3">
        <button
          className="btn-kids btn-kids-green w-100 py-3 fs-5 d-flex align-items-center justify-content-center gap-2"
          onClick={handleRunCode}
          disabled={isRunning || isPyodideLoading}
        >
          <Play size={22} fill="white" />
          <span>{isRunning ? 'Đang chạy thử...' : 'Bấm để Chạy thử! 🚀'}</span>
        </button>
      </div>

      {/* Terminal ảo */}
      <div className="terminal-container">
        <div className="terminal-header">
          <div className="d-flex align-items-center gap-2">
            <TerminalIcon size={16} className="text-muted" />
            <span className="terminal-title">BẢNG KẾT QUẢ HIỂN THỊ</span>
          </div>
        </div>
        <div className="terminal-output">
          {output.length === 0 ? (
            <div className="output-empty">Kết quả chạy code của bé sẽ hiện ra ở đây... Nhấn nút chạy phía trên nhé! 🌟</div>
          ) : (
            output.map((line, idx) => (
              <div 
                key={idx} 
                className={`output-line ${
                  line.type === 'error' ? 'output-error' : 
                  line.type === 'success' ? 'output-success' : 
                  line.type === 'info' ? 'text-info' : 'text-light'
                }`}
              >
                {line.text}
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

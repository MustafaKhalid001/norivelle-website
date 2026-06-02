document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileBtn && navLinks) {
        mobileBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const themeIcon = themeToggleBtn?.querySelector('i');

    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    } else {
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            htmlElement.setAttribute('data-theme', 'dark');
            updateThemeIcon('dark');
        }
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = htmlElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if (theme === 'dark') {
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
        } else {
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
        }
    }

    // Contact Form File Upload Label Update
    const fileInput = document.getElementById('attachment');
    const fileNameDisplay = document.querySelector('.file-name');

    if (fileInput && fileNameDisplay) {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                if (e.target.files.length === 1) {
                    fileNameDisplay.textContent = e.target.files[0].name;
                } else {
                    fileNameDisplay.textContent = `${e.target.files.length} files selected`;
                }
            } else {
                fileNameDisplay.textContent = 'No file chosen';
            }
        });
    }

    // FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            // Optional: Close all other FAQs
            // faqItems.forEach(i => i.classList.remove('active'));
            if (!isActive) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
    });

    // Header scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = 'var(--shadow)';
        } else {
            header.style.boxShadow = 'none';
        }
    });

    // Contact Form Submission
    const contactForms = document.querySelectorAll('.norivelle-form');
    contactForms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'Sending...';
            submitBtn.disabled = true;

            try {
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());
                data.services = formData.getAll('service');

                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                });

                const result = await response.json();

                if (response.ok) {
                    alert('Thank you! Your message has been sent successfully.');
                    form.reset();
                } else {
                    alert('Error: ' + (result.error || 'Failed to send message. Please try again.'));
                }
            } catch (error) {
                console.error('Submission error:', error);
                alert('An unexpected error occurred. Please try again later.');
            } finally {
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            }
        });
    });

    // Favicon Injection
    const favicon = document.createElement('link');
    favicon.rel = 'icon';
    favicon.href = 'images/logo.png';
    favicon.type = 'image/png';
    document.head.appendChild(favicon);

    // --- AI Chatbot Injection & Logic ---
    const chatbotStyles = document.createElement('style');
    chatbotStyles.innerHTML = `
        /* Chatbot CSS */
        #nv-chatbot-container {
            position: fixed;
            bottom: 30px;
            left: 30px;
            z-index: 999999;
            font-family: 'Inter', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        
        #nv-chatbot-button {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(139, 92, 246, 0.4);
            transition: all 0.3s ease;
            z-index: 2;
        }
        
        #nv-chatbot-button:hover {
            transform: scale(1.1) translateY(-5px);
            box-shadow: 0 15px 35px rgba(139, 92, 246, 0.6);
        }

        #nv-chatbot-window {
            position: absolute;
            bottom: 80px;
            left: 0;
            width: 350px;
            height: 500px;
            background: var(--card-bg, #ffffff);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            opacity: 0;
            transform: scale(0.8) translateY(20px);
            transform-origin: bottom left;
            pointer-events: none;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: 1;
        }
        
        /* For dark theme compatibility */
        [data-theme='dark'] #nv-chatbot-window {
            background: #1e1e2e;
            border-color: rgba(255,255,255,0.1);
        }

        #nv-chatbot-window.open {
            opacity: 1;
            transform: scale(1) translateY(0);
            pointer-events: auto;
        }

        #nv-chatbot-header {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 600;
        }

        #nv-chatbot-close {
            cursor: pointer;
            font-size: 18px;
            transition: transform 0.2s;
        }
        #nv-chatbot-close:hover {
            transform: scale(1.2);
        }

        #nv-chatbot-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
            background: var(--bg-color, #f8fafc);
        }

        [data-theme='dark'] #nv-chatbot-messages {
            background: #11111b;
        }

        .nv-chat-bubble {
            max-width: 80%;
            padding: 12px 16px;
            border-radius: 18px;
            font-size: 14px;
            line-height: 1.4;
            animation: nvFadeInUp 0.3s ease;
        }

        .nv-chat-bot {
            background: var(--card-bg, #ffffff);
            color: var(--text-color, #333333);
            border: 1px solid rgba(139, 92, 246, 0.1);
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }
        
        [data-theme='dark'] .nv-chat-bot {
            background: #1e1e2e;
            color: #e2e8f0;
            border-color: rgba(255,255,255,0.05);
        }

        .nv-chat-user {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
            box-shadow: 0 4px 10px rgba(139, 92, 246, 0.2);
        }

        #nv-chatbot-input-container {
            padding: 15px;
            background: var(--card-bg, #ffffff);
            border-top: 1px solid rgba(139, 92, 246, 0.1);
            display: flex;
            gap: 10px;
        }
        
        [data-theme='dark'] #nv-chatbot-input-container {
            background: #1e1e2e;
            border-color: rgba(255,255,255,0.05);
        }

        #nv-chatbot-input {
            flex: 1;
            padding: 12px 15px;
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 20px;
            outline: none;
            font-family: inherit;
            background: var(--bg-color, #f8fafc);
            color: var(--text-color, #333);
            transition: border-color 0.3s;
        }
        
        [data-theme='dark'] #nv-chatbot-input {
            background: #11111b;
            color: #e2e8f0;
            border-color: rgba(255,255,255,0.1);
        }

        #nv-chatbot-input:focus {
            border-color: var(--primary);
        }

        #nv-chatbot-send {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: var(--primary);
            color: white;
            border: none;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: transform 0.2s, background 0.3s;
        }

        #nv-chatbot-send:hover {
            transform: scale(1.1);
            background: var(--accent);
        }
        
        #nv-chatbot-send:disabled {
            background: #ccc;
            transform: none;
            cursor: not-allowed;
        }

        .nv-typing-indicator {
            display: flex;
            gap: 4px;
            padding: 15px;
            align-items: center;
        }
        .nv-dot {
            width: 6px;
            height: 6px;
            background: var(--primary);
            border-radius: 50%;
            animation: nvBlink 1.4s infinite both;
        }
        .nv-dot:nth-child(1) { animation-delay: 0s; }
        .nv-dot:nth-child(2) { animation-delay: 0.2s; }
        .nv-dot:nth-child(3) { animation-delay: 0.4s; }

        @keyframes nvFadeInUp {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes nvBlink {
            0% { opacity: 0.2; transform: scale(0.8); }
            20% { opacity: 1; transform: scale(1.2); }
            100% { opacity: 0.2; transform: scale(0.8); }
        }
        
        /* Mobile Responsiveness */
        @media (max-width: 480px) {
            #nv-chatbot-window {
                width: calc(100vw - 40px);
                height: 400px;
            }
        }
    `;
    document.head.appendChild(chatbotStyles);

    const chatbotHTML = `
        <div id="nv-chatbot-container">
            <div id="nv-chatbot-window">
                <div id="nv-chatbot-header">
                    <div><i class="fa-solid fa-robot" style="margin-right: 8px;"></i> Norivelle Assistant</div>
                    <div id="nv-chatbot-close"><i class="fa-solid fa-xmark"></i></div>
                </div>
                <div id="nv-chatbot-messages">
                    <div class="nv-chat-bubble nv-chat-bot">Hi there! 👋 I'm the Norivelle AI assistant. How can I help you with your digital needs today?</div>
                </div>
                <div id="nv-chatbot-input-container">
                    <input type="text" id="nv-chatbot-input" placeholder="Type your message..." autocomplete="off">
                    <button id="nv-chatbot-send"><i class="fa-solid fa-paper-plane"></i></button>
                </div>
            </div>
            <div id="nv-chatbot-button">
                <i class="fa-solid fa-message"></i>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', chatbotHTML);

    // Chatbot Logic
    const chatBtn = document.getElementById('nv-chatbot-button');
    const chatWindow = document.getElementById('nv-chatbot-window');
    const closeBtn = document.getElementById('nv-chatbot-close');
    const inputField = document.getElementById('nv-chatbot-input');
    const sendBtn = document.getElementById('nv-chatbot-send');
    const messagesContainer = document.getElementById('nv-chatbot-messages');

    // Toggle Chat Window
    const toggleChat = () => {
        const isOpen = chatWindow.classList.contains('open');
        if (isOpen) {
            chatWindow.classList.remove('open');
            chatBtn.innerHTML = '<i class="fa-solid fa-message"></i>';
        } else {
            chatWindow.classList.add('open');
            chatBtn.innerHTML = '<i class="fa-solid fa-chevron-down"></i>';
            inputField.focus();
        }
    };

    chatBtn.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);

    let chatHistory = [];

    const addMessageToUI = (text, isUser) => {
        const bubble = document.createElement('div');
        bubble.className = `nv-chat-bubble ${isUser ? 'nv-chat-user' : 'nv-chat-bot'}`;
        bubble.textContent = text;
        messagesContainer.appendChild(bubble);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    };

    const showTypingIndicator = () => {
        const indicator = document.createElement('div');
        indicator.className = 'nv-chat-bubble nv-chat-bot nv-typing-indicator';
        indicator.id = 'nv-typing';
        indicator.innerHTML = '<div class="nv-dot"></div><div class="nv-dot"></div><div class="nv-dot"></div>';
        messagesContainer.appendChild(indicator);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    };

    const removeTypingIndicator = () => {
        const indicator = document.getElementById('nv-typing');
        if (indicator) indicator.remove();
    };

    const handleSend = async () => {
        const text = inputField.value.trim();
        if (!text) return;

        // User message
        addMessageToUI(text, true);
        inputField.value = '';
        inputField.disabled = true;
        sendBtn.disabled = true;
        
        chatHistory.push({ role: 'user', content: text });
        
        showTypingIndicator();

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ messages: chatHistory })
            });

            removeTypingIndicator();

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.error || 'Server error');
            }

            const data = await response.json();
            const aiReply = data.reply;
            
            addMessageToUI(aiReply, false);
            chatHistory.push({ role: 'assistant', content: aiReply });

        } catch (error) {
            removeTypingIndicator();
            console.error('Chat API Error:', error);
            addMessageToUI("Sorry, I'm having trouble connecting to my brain right now. Please try again later!", false);
        } finally {
            inputField.disabled = false;
            sendBtn.disabled = false;
            inputField.focus();
        }
    };

    sendBtn.addEventListener('click', handleSend);
    inputField.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

});

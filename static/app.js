// Orion Voice Assistant - Futuristic Frontend

let isListening = false;
let recognition = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    setupEventListeners();
    createStarfield();
    updateDateTime();
    
    // Load saved settings
    loadSettingsValues();
    applySettings();
    
    // Update time every second
    setInterval(updateDateTime, 1000);
    
    // Load voices for TTS
    if ('speechSynthesis' in window) {
        speechSynthesis.getVoices(); // Load voices
        if (speechSynthesis.onvoiceschanged !== undefined) {
            speechSynthesis.onvoiceschanged = () => {
                console.log('Voices loaded');
            };
        }
    }
    
    // Setup Web Speech API if available
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        setupSpeechRecognition();
    } else {
        console.warn('Speech recognition not supported in this browser');
        document.getElementById('micBtn').disabled = true;
        document.getElementById('micBtn').title = 'Speech recognition not supported';
    }
});

function initializeApp() {
    console.log('🤖 Orion Futuristic Interface Initialized');
}

function createStarfield() {
    const starfield = document.getElementById('starfield');
    const starCount = 200;
    
    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.style.position = 'absolute';
        star.style.width = Math.random() * 2 + 'px';
        star.style.height = star.style.width;
        star.style.background = 'white';
        star.style.borderRadius = '50%';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.opacity = Math.random() * 0.5 + 0.3;
        star.style.animation = `twinkle ${Math.random() * 3 + 2}s ease-in-out infinite`;
        star.style.animationDelay = Math.random() * 3 + 's';
        starfield.appendChild(star);
    }
}

function updateDateTime() {
    const now = new Date();
    
    // Update time
    const timeEl = document.getElementById('currentTime');
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    const displayHours = hours % 12 || 12;
    timeEl.textContent = `${displayHours}:${minutes.toString().padStart(2, '0')} ${ampm}`;
    
    // Update date
    const dateEl = document.getElementById('currentDate');
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    dateEl.textContent = `${days[now.getDay()]}, ${months[now.getMonth()]} ${now.getDate()}`;
}

// Settings object to store user preferences
let settings = {
    voiceRate: 0.95,  // Slower, more natural
    voicePitch: 1.0,  // Natural pitch
    voiceVolume: 1.0,
    animationSpeed: 1,
    enableParticles: true,
    enableGlow: true,
    autoSpeak: true,
    showTimestamp: true,
    themeColor: 'cyan'
};

function setupEventListeners() {
    const micBtn = document.getElementById('micBtn');
    const keyboardBtn = document.getElementById('keyboardBtn');
    const settingsBtn = document.getElementById('settingsBtn');
    const textInput = document.getElementById('textInput');
    const sendBtn = document.getElementById('sendBtn');
    const inputContainer = document.getElementById('inputContainer');
    
    // Microphone button
    micBtn.addEventListener('click', toggleVoiceRecognition);
    
    // Settings button
    settingsBtn.addEventListener('click', openSettings);
    
    // Keyboard button - toggle input
    keyboardBtn.addEventListener('click', function(e) {
        e.stopPropagation(); // Prevent triggering document click
        if (inputContainer.style.display === 'none' || !inputContainer.style.display) {
            inputContainer.style.display = 'flex';
            textInput.focus();
        } else {
            inputContainer.style.display = 'none';
        }
    });
    
    // Send button
    sendBtn.addEventListener('click', function() {
        sendCommand(textInput.value);
        textInput.value = '';
        inputContainer.style.display = 'none'; // Hide after sending
    });
    
    // Enter key in text input
    textInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendCommand(textInput.value);
            textInput.value = '';
            inputContainer.style.display = 'none'; // Hide after sending
        }
    });
    
    // Click outside to close text input
    document.addEventListener('click', function(e) {
        if (inputContainer.style.display === 'flex') {
            // Check if click is outside input container and keyboard button
            if (!inputContainer.contains(e.target) && e.target !== keyboardBtn && !keyboardBtn.contains(e.target)) {
                inputContainer.style.display = 'none';
            }
        }
    });
    
    // Prevent closing when clicking inside input container
    inputContainer.addEventListener('click', function(e) {
        e.stopPropagation();
    });
    
    // Settings modal event listeners
    setupSettingsListeners();
}

function openSettings() {
    const modal = document.getElementById('settingsModal');
    modal.style.display = 'flex';
    loadSettingsValues();
}

function closeSettings() {
    const modal = document.getElementById('settingsModal');
    modal.style.display = 'none';
}

function setupSettingsListeners() {
    const closeBtn = document.getElementById('closeSettings');
    const saveBtn = document.getElementById('saveSettings');
    const resetBtn = document.getElementById('resetSettings');
    const modal = document.getElementById('settingsModal');
    
    // Close button
    closeBtn.addEventListener('click', closeSettings);
    
    // Click outside to close
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeSettings();
        }
    });
    
    // Save settings
    saveBtn.addEventListener('click', saveSettings);
    
    // Reset settings
    resetBtn.addEventListener('click', resetSettings);
    
    // Real-time updates for sliders
    const sliders = ['voiceRate', 'voicePitch', 'voiceVolume', 'animationSpeed'];
    sliders.forEach(sliderId => {
        const slider = document.getElementById(sliderId);
        const valueSpan = document.getElementById(sliderId + 'Value');
        
        slider.addEventListener('input', function() {
            let value = parseFloat(this.value);
            if (sliderId === 'voiceVolume') {
                valueSpan.textContent = Math.round(value * 100) + '%';
            } else {
                valueSpan.textContent = value + 'x';
            }
            
            // Apply setting immediately
            settings[sliderId] = value;
            if (sliderId === 'animationSpeed') {
                updateAnimationSpeed(value);
            }
        });
    });
}

function loadSettingsValues() {
    // Load saved settings from localStorage
    const saved = localStorage.getItem('orionSettings');
    if (saved) {
        settings = { ...settings, ...JSON.parse(saved) };
    }
    
    // Update UI elements
    document.getElementById('voiceRate').value = settings.voiceRate;
    document.getElementById('voiceRateValue').textContent = settings.voiceRate + 'x';
    
    document.getElementById('voicePitch').value = settings.voicePitch;
    document.getElementById('voicePitchValue').textContent = settings.voicePitch + 'x';
    
    document.getElementById('voiceVolume').value = settings.voiceVolume;
    document.getElementById('voiceVolumeValue').textContent = Math.round(settings.voiceVolume * 100) + '%';
    
    document.getElementById('animationSpeed').value = settings.animationSpeed;
    document.getElementById('animationSpeedValue').textContent = settings.animationSpeed + 'x';
    
    document.getElementById('enableParticles').checked = settings.enableParticles;
    document.getElementById('enableGlow').checked = settings.enableGlow;
    document.getElementById('autoSpeak').checked = settings.autoSpeak;
    document.getElementById('showTimestamp').checked = settings.showTimestamp;
    document.getElementById('themeColor').value = settings.themeColor;
}

function saveSettings() {
    // Get all values from form
    settings.voiceRate = parseFloat(document.getElementById('voiceRate').value);
    settings.voicePitch = parseFloat(document.getElementById('voicePitch').value);
    settings.voiceVolume = parseFloat(document.getElementById('voiceVolume').value);
    settings.animationSpeed = parseFloat(document.getElementById('animationSpeed').value);
    settings.enableParticles = document.getElementById('enableParticles').checked;
    settings.enableGlow = document.getElementById('enableGlow').checked;
    settings.autoSpeak = document.getElementById('autoSpeak').checked;
    settings.showTimestamp = document.getElementById('showTimestamp').checked;
    settings.themeColor = document.getElementById('themeColor').value;
    
    // Save to localStorage
    localStorage.setItem('orionSettings', JSON.stringify(settings));
    
    // Apply settings
    applySettings();
    
    // Show confirmation
    document.getElementById('statusText').textContent = 'Settings saved successfully!';
    setTimeout(() => {
        document.getElementById('statusText').textContent = 'Waiting for your command...';
    }, 2000);
    
    closeSettings();
}

function resetSettings() {
    // Reset to defaults
    settings = {
        voiceRate: 0.95,  // Slower, more natural
        voicePitch: 1.0,  // Natural pitch
        voiceVolume: 1.0,
        animationSpeed: 1,
        enableParticles: true,
        enableGlow: true,
        autoSpeak: true,
        showTimestamp: true,
        themeColor: 'cyan'
    };
    
    // Update UI
    loadSettingsValues();
    
    // Apply settings
    applySettings();
}

function applySettings() {
    // Apply animation speed
    updateAnimationSpeed(settings.animationSpeed);
    
    // Apply theme color
    updateThemeColor(settings.themeColor);
    
    // Apply glow effects
    const orbElements = document.querySelectorAll('.orbit, .orbital-ring, .main-orb');
    orbElements.forEach(el => {
        if (settings.enableGlow) {
            el.style.filter = 'url(#glow)';
        } else {
            el.style.filter = 'none';
        }
    });
}

function updateAnimationSpeed(speed) {
    const style = document.createElement('style');
    style.textContent = `
        .orbit-1 { animation-duration: ${16/speed}s, ${3/speed}s, ${2.5/speed}s !important; }
        .orbit-2 { animation-duration: ${24/speed}s, ${4.5/speed}s, ${3.5/speed}s !important; }
        .orbit-3 { animation-duration: ${32/speed}s, ${5/speed}s, ${4/speed}s !important; }
        .orbital-ring { animation-duration: ${28/speed}s, ${6/speed}s !important; }
        .main-orb { animation-duration: ${4/speed}s, ${3/speed}s !important; }
    `;
    
    // Remove old speed style if exists
    const oldStyle = document.getElementById('animation-speed-style');
    if (oldStyle) oldStyle.remove();
    
    style.id = 'animation-speed-style';
    document.head.appendChild(style);
}

function updateThemeColor(color) {
    const colors = {
        cyan: '#00f0ff',
        purple: '#8b5cf6',
        green: '#10b981',
        orange: '#f97316',
        pink: '#ec4899'
    };
    
    const newColor = colors[color] || colors.cyan;
    
    // Update CSS custom property
    document.documentElement.style.setProperty('--primary-cyan', newColor);
}

function setupSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';
    
    recognition.onstart = function() {
        console.log('Voice recognition started');
        isListening = true;
        document.getElementById('micBtn').classList.add('listening');
        document.getElementById('statusText').textContent = 'Listening...';
    };
    
    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        console.log('Recognized:', transcript);
        sendCommand(transcript);
    };
    
    recognition.onerror = function(event) {
        console.error('Speech recognition error:', event.error);
        isListening = false;
        document.getElementById('micBtn').classList.remove('listening');
        document.getElementById('statusText').textContent = 'Error - please try again';
        
        if (event.error === 'no-speech') {
            document.getElementById('statusText').textContent = 'No speech detected';
        } else if (event.error === 'not-allowed') {
            document.getElementById('statusText').textContent = 'Microphone access denied';
        }
    };
    
    recognition.onend = function() {
        console.log('Voice recognition ended');
        isListening = false;
        document.getElementById('micBtn').classList.remove('listening');
        if (document.getElementById('statusText').textContent === 'Listening...') {
            document.getElementById('statusText').textContent = 'Waiting for your command...';
        }
    };
}

function toggleVoiceRecognition() {
    if (!recognition) {
        document.getElementById('statusText').textContent = 'Speech recognition not available';
        return;
    }
    
    if (isListening) {
        recognition.stop();
    } else {
        recognition.start();
    }
}

async function sendCommand(command) {
    if (!command || !command.trim()) return;
    
    command = command.trim();
    const originalCommand = command;
    
    // Show user message with original text
    showUserMessage(originalCommand);
    
    // Add loading animation
    const statusEl = document.getElementById('statusText');
    let dots = 0;
    const loadingInterval = setInterval(() => {
        dots = (dots + 1) % 4;
        statusEl.textContent = 'Processing' + '.'.repeat(dots);
    }, 400);
    
    try {
        const response = await fetch('/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: command })
        });
        
        // Clear loading animation
        clearInterval(loadingInterval);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Show assistant response
        showAssistantMessage(data.response);
        statusEl.textContent = 'Waiting for your command...';
        
        // Speak the response
        speakText(data.response);
        
        // Handle special commands (use lowercase for matching)
        handleSpecialCommands(command.toLowerCase(), data.response);
        
    } catch (error) {
        clearInterval(loadingInterval);
        console.error('Error sending command:', error);
        
        // More specific error messages
        let errorMsg = 'Sorry, something went wrong. Please try again.';
        if (!navigator.onLine) {
            errorMsg = 'No internet connection. Please check your network.';
        }
        
        showAssistantMessage(errorMsg);
        statusEl.textContent = 'Error - click to retry';
    }
}

function showUserMessage(text) {
    const userMsg = document.getElementById('userMessage');
    userMsg.textContent = text;
    userMsg.style.display = 'block';
    
    // Hide after 3 seconds
    setTimeout(() => {
        userMsg.style.display = 'none';
    }, 3000);
}

function showAssistantMessage(text) {
    const assistantMsg = document.getElementById('assistantMessage');
    assistantMsg.innerHTML = `<p>${escapeHtml(text)}</p>`;
}


function speakText(text) {
    // Check if auto-speak is enabled
    if (!settings.autoSpeak) return;
    
    // Use Web Speech API for TTS with user settings
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        
        // Get available voices and select the best quality one
        const voices = window.speechSynthesis.getVoices();
        
        // Priority order for voice selection (best quality first)
        const voicePriority = [
            'Google US English',
            'Google UK English Female',
            'Microsoft David',
            'Microsoft Zira',
            'Samantha',
            'Alex',
            'Google UK English Male',
            'Microsoft Mark'
        ];
        
        // Try to find the best available voice
        let selectedVoice = null;
        for (const voiceName of voicePriority) {
            selectedVoice = voices.find(voice => voice.name.includes(voiceName));
            if (selectedVoice) break;
        }
        
        // Fallback to any English voice if none found
        if (!selectedVoice) {
            selectedVoice = voices.find(voice => 
                voice.lang.startsWith('en') && !voice.name.includes('eSpeak')
            );
        }
        
        if (selectedVoice) {
            utterance.voice = selectedVoice;
            console.log('Using voice:', selectedVoice.name);
        }
        
        // Use settings values for natural speech
        utterance.rate = settings.voiceRate;
        utterance.pitch = settings.voicePitch;
        utterance.volume = settings.voiceVolume;
        utterance.lang = 'en-US';
        
        window.speechSynthesis.speak(utterance);
    }
}

function handleSpecialCommands(command, response) {
    // command is already lowercase from sendCommand function
    
    // Open websites in new tab
    if (command.includes('open')) {
        if (command.includes('google')) {
            window.open('https://google.com', '_blank');
        } else if (command.includes('youtube')) {
            window.open('https://youtube.com', '_blank');
        } else if (command.includes('facebook')) {
            window.open('https://facebook.com', '_blank');
        } else if (command.includes('linkedin')) {
            window.open('https://linkedin.com', '_blank');
        }
    }
    
    // Play music - handle both "play perfect" and "play Perfect"
    if (command.includes('play ')) {
        loadAndPlaySong(command);
    }
}

async function loadAndPlaySong(command) {
    try {
        const response = await fetch('/api/songs');
        const data = await response.json();
        
        // Extract song name: handle "play perfect", "Play Perfect", etc.
        let songName = command.replace(/^play\s+/i, '').trim().toLowerCase();
        
        // Convert spaces to underscores for matching library keys
        const songKey = songName.replace(/\s+/g, '_');
        
        console.log('Searching for song:', songKey); // Debug log
        
        const song = data.songs.find(s => s.key === songKey);
        
        if (song) {
            console.log('Playing:', song.name);
            window.open(song.url, '_blank');
        } else {
            console.log('Song not found. Available keys:', data.songs.map(s => s.key));
        }
    } catch (error) {
        console.error('Error loading songs:', error);
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

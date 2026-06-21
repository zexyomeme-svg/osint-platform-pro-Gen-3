# 📂 Project Blueprint & UI Specification

This document provides a detailed map of the Nexus Intelligence Framework's internal structure and a specification of its user interface.

## 🗺️ File & Folder Hierarchy

```text
nexus-osint/
├── app/                         # Core Application Logic
│   ├── main.py                  # Flask Application & API Routing
│   ├── utils.py                 # OSINT Intelligence Engines (The "Brains")
│   ├── optimizer.py             # Resource Monitoring & Memory Cleanup
│   ├── system_manager.py        # Pre-flight Integrity & Update Checks
│   ├── static/                  # Frontend Assets
│   │   ├── css/                 # Custom Stylesheets
│   │   └── js/                   # Frontend Logic
│   └── templates/               # UI Layouts (Jinja2 HTML)
│       ├── base.html            # Global Layout & Dark Theme Config
│       ├── index.html           # Main Dashboard
│       ├── ip_lookup.html       # IP Intel Interface
│       ├── domain_lookup.html   # Domain Intel Interface
│       ├── identity_lookup.html # Identity Mapping Interface
│       ├── email_lookup.html    # Email Intel Interface
│       ├── phone_lookup.html    # Phone Intel Interface
│       └── stats.html           # System Telemetry Interface
├── run.py                       # Application Entry Point (Bootloader)
├── requirements.txt             # Python Dependencies
├── Procfile                     # Render Deployment Configuration
└── README.md                    # Project Documentation
```

## 🎨 UI/UX Specification

### 1. Visual Theme: "Cyber-Intelligence Dark"
- **Background**: Deep Zinc (`#09090b`) to reduce eye strain and evoke a security-ops center feel.
- **Card Style**: Glassmorphism (`rgba(24, 24, 27, 0.7)`) with 12px backdrop blur and subtle borders.
- **Color Coding**:
    - 🔵 **Blue**: IP & Email Intelligence (Trust & Communication).
    - 🟣 **Purple**: Domain Intelligence (Infrastructure).
    - 🟢 **Emerald**: Identity & Phone Intelligence (Human Intelligence).
    - ⚪ **Zinc/Grey**: System Telemetry (Hardware).

### 2. Layout Architecture
- **Global Navigation**: A sticky glass-header with a pulsating "System Live" indicator showing real-time RAM usage.
- **Dashboard**: A responsive grid of "Intelligence Modules." Each module features a hover-animation that lifts the card and glows in its assigned accent color.
- **Tool Pages**: 
    - **Top Section**: High-contrast input field with a "Neon" glow effect on focus.
    - **Mid Section**: A simulated analysis progress bar that provides visual feedback during API calls.
    - **Bottom Section**: Results displayed in "Intelligence Profiles"—structured data cards that avoid cluttered tables in favor of a clean, labeled attribute list.

### 3. User Experience (UX) Flow
1. **Boot**: `run.py` triggers a system audit $\rightarrow$ Log output $\rightarrow$ Web Server launch.
2. **Analysis**: User enters target $\rightarrow$ Progress bar animates (simulating deep scan) $\rightarrow$ Results fade in from the bottom using CSS transitions.
3. **Optimization**: User monitors RAM on the Telemetry page $\rightarrow$ Clicks "Force Optimization" $\rightarrow$ Backend triggers `gc.collect()` $\rightarrow$ RAM bar drops in real-time.

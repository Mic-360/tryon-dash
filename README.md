# TryOn Dashboard

A modern, feature-rich dashboard built with [Reflex](https://reflex.dev) for managing TryOn virtual try-on services. Features a beautiful dark theme using the Catppuccin Mocha color palette design system.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Reflex](https://img.shields.io/badge/Reflex-0.8.26-purple?logo=react&logoColor=white)

## ✨ Features

### Dashboard

- 📊 **Business Overview** - View all registered businesses with key metrics
- 🔑 **API Key Management** - Toggle visibility of API keys with secure masking
- ➕ **Add Business** - Modal dialog for creating new business accounts
- 📈 **Statistics Cards** - Quick glance metrics (Total Businesses, Active Today, API Calls, Success Rate)

### Logs Viewer

- 📜 **Real-time Logs** - View processing logs with auto-refresh capability
- 🔍 **Advanced Filtering** - Filter by User ID, Business ID, Product ID, Cloth Type, and more
- 🖼️ **Image Previews** - View person, cloth, and result images inline
- 📅 **Date Filtering** - Filter logs by date range

### UI/UX

- 🌙 **Dark Theme** - Beautiful Catppuccin Mocha color palette
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 🎨 **Modern Design** - shadcn-inspired component styling
- ↔️ **Collapsible Sidebar** - Space-efficient navigation

## 🛠️ Tech Stack

- **Framework**: [Reflex](https://reflex.dev) - Pure Python web framework
- **Styling**: [TailwindCSS v4](https://tailwindcss.com) via Reflex plugin
- **Theme**: [Catppuccin Mocha](https://catppuccin.com) - Soothing pastel dark theme
- **HTTP Client**: [httpx](https://www.python-httpx.org) - Async HTTP requests
- **Icons**: [Lucide Icons](https://lucide.dev) - Beautiful open-source icons

## 📁 Project Structure

```
tryon-dash/
├── assets/                 # Static assets (images, fonts)
├── tryon_dash/
│   ├── __init__.py
│   ├── tryon_dash.py       # Main app entry point
│   ├── state.py            # Application state management
│   ├── components/
│   │   ├── __init__.py
│   │   ├── sidebar.py      # Collapsible sidebar navigation
│   │   └── layout.py       # Main layout wrapper
│   └── pages/
│       ├── __init__.py
│       ├── dashboard.py    # Dashboard/Home page
│       └── logs.py         # Logs viewer page
├── rxconfig.py             # Reflex configuration
├── requirements.txt        # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd tryon-dash
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Reflex** (first time only)

   ```bash
   reflex init
   ```

5. **Run the development server**

   ```bash
   reflex run
   ```

6. **Open your browser**
   Navigate to `http://localhost:3000`

## 🚀 Deploy

### Build directory: `.web`

### Build Command:
```bash
npm run export
```
### Run Command:
```bash
npm run prod
```
Deploy to any static host.

## 📖 Usage

### Dashboard Page (`/`)

- View all registered businesses in a table
- Click the eye icon to reveal/hide API keys
- Click "Add Business" to create a new business account
- Use the "Refresh" button to reload data

### Logs Page (`/logs`)

- View all processing logs with image previews
- Use filters to narrow down results:
  - **ID Filters**: User ID, Business ID, Product ID, Cloth Type
  - **Technical Filters**: Inference Steps, Seed, Guidance Scale, Date
- Click "Clear All" to reset all filters
- Click "Refresh" to load latest logs

## 🎨 Color Palette

This project uses the **Catppuccin Mocha** color palette:

| Color    | Hex       | Usage                  |
| -------- | --------- | ---------------------- |
| Base     | `#1e1e2e` | Main background        |
| Mantle   | `#181825` | Card backgrounds       |
| Surface0 | `#313244` | Input backgrounds      |
| Text     | `#cdd6f4` | Primary text           |
| Mauve    | `#cba6f7` | Accent/Primary buttons |
| Blue     | `#89b4fa` | Info elements          |
| Green    | `#a6e3a1` | Success states         |
| Peach    | `#fab387` | Warning elements       |
| Red      | `#f38ba8` | Error states           |

## 🔧 Configuration

Reflex configuration is in `rxconfig.py`:

```python
import reflex as rx

config = rx.Config(
    app_name="tryon_dash",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
```

## 📝 API Endpoints

The dashboard connects to the following API endpoints:

| Endpoint                            | Method | Description               |
| ----------------------------------- | ------ | ------------------------- |
| `/api/v1/internal/getAllBusinesses` | GET    | Fetch all businesses      |
| `/api/v1/internal/createBusiness`   | POST   | Create a new business     |
| `/api/v1/internal/getAllLogs`       | GET    | Fetch all processing logs |

<p align="center">
  Made with ☕ by <a href="https://twinverse.in">Bhaumic</a>
</p>

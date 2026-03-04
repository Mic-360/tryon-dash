# TryOn Dash - Internal Admin Dashboard

TryOn Dash is an internal monitoring and management platform for Twinverse Tech's virtual try-on services. It empowers admins to manage business partnerships and monitor processing logs in real-time.

![TryOn Dash UI](https://twinverse.in/favicon.ico)

## 🚀 Key Features

### 🏢 Business Management
- **Centralized Directory**: View all registered businesses with their associated metadata.
- **Seamless Registration**: Add new business partners via a dedicated interface.
- **API Key Control**: Manage at-a-glance or obscure sensitive API keys for security.

### 📊 Logs & Analytics
- **Live Stream**: Auto-refreshing logs (every 60s) to monitor visual try-on requests.
- **Deep-Dive Filters**: Filter logs by User ID, Business ID, Product ID, Cloth Type, and technical parameters (Seed, Guidance Scale, etc.).
- **Visual Verification**: Direct visual comparison of:
  - **Person Image**: The base model/user input.
  - **Cloth Image**: The selected garment.
  - **Result Image**: The AI-generated output.

## 🛠️ Tech Stack

- **Frontend**: [React](https://reactjs.org/) with [TypeScript](https://www.typescriptlang.org/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **Routing**: [TanStack Router](https://tanstack.com/router)
- **State Management**: [Redux Toolkit](https://redux-toolkit.js.org/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Data Table**: [TanStack Table](https://tanstack.com/table)

## 📂 Project Structure

- `src/store`: Redux store and slices for global state (Businesses).
- `src/Layout.tsx`: Main application wrapper with a responsive sidebar.
- `src/Sidebar.tsx`: Sidebar component with collapse/expand and mobile-responsive overlays.
- `src/App.tsx`: Home dashboard for business management.
- `src/Logs.tsx`: Real-time logging dashboard with advanced filtering.

## ⚙️ Getting Started

### Prerequisites

- Node.js (Active LTS)
- Yarn (`v4.5.1` recommended)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   yarn install
   ```

### Development

Run the local development server:
```bash
yarn dev
```

### Build

Create a production build:
```bash
yarn build
```

The application connects to the production backend at `https://twinverses.in` by default (see `src/config.ts`).

---
Developed by **[Twinverse Tech](https://twinverse.in)**

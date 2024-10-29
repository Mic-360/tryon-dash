import React, { createContext, useContext, useState, useEffect } from 'react';
import { Link } from '@tanstack/react-router';
import { Menu, X, ChevronLeft, ChevronRight } from 'lucide-react';

// Context for sidebar state
const SidebarContext = createContext<{
  isOpen: boolean;
  isCollapsed: boolean;
  toggleSidebar: () => void;
  toggleCollapse: () => void;
} | null>(null);

// Hook to use sidebar context
const useSidebar = () => {
  const context = useContext(SidebarContext);
  if (!context) {
    throw new Error('useSidebar must be used within a SidebarProvider');
  }
  return context;
};

// Sidebar provider component
export const SidebarProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isCollapsed, setIsCollapsed] = useState(false);
  const toggleSidebar = () => setIsOpen(!isOpen);
  const toggleCollapse = () => setIsCollapsed(!isCollapsed);

  return (
    <SidebarContext.Provider
      value={{ isOpen, isCollapsed, toggleSidebar, toggleCollapse }}
    >
      {children}
    </SidebarContext.Provider>
  );
};

// Main Sidebar component
export const Sidebar: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const { isOpen, isCollapsed, toggleSidebar, toggleCollapse } = useSidebar();
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const checkMobile = () => setIsMobile(window.innerWidth < 768);
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  return (
    <>
      {/* Mobile overlay */}
      {isMobile && isOpen && (
        <div
          className='fixed inset-0 bg-black bg-opacity-50 z-20'
          onClick={toggleSidebar}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`fixed top-0 left-0 z-30 h-full bg-white shadow-lg transform transition-all duration-300 ease-in-out ${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        } ${isCollapsed ? 'w-16' : 'w-64'} md:relative md:translate-x-0`}
      >
        <div className='flex flex-col h-full'>{children}</div>

        {/* Collapse toggle button */}
        <button type='button'
          onClick={toggleCollapse}
          className='absolute top-2 -right-3 bg-gray-400 rounded-full p-1 shadow-md hidden md:block'
        >
          {isCollapsed ? <ChevronRight size={20} /> : <ChevronLeft size={20} />}
        </button>
      </aside>

      {/* Mobile toggle button */}
      <button
        type='button'
        onClick={toggleSidebar}
        className='fixed top-4 left-4 z-40 md:hidden bg-white p-2 rounded-md shadow-md'
      >
        {isOpen ? <X size={24} /> : <Menu size={24} />}
      </button>
    </>
  );
};

// Subcomponents
export const SidebarHeader: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const { isCollapsed } = useSidebar();

  const renderCollapsedContent = () => {
    if (React.isValidElement(children)) {
      const childText = children.props.children;
      if (typeof childText === 'string') {
        return childText.charAt(0).toUpperCase();
      }
    } else if (typeof children === 'string') {
      return children.charAt(0).toUpperCase();
    }
    return 'D';
  };

  return (
    <div className={`p-4 border-b ${isCollapsed ? 'text-center' : ''}`}>
      {isCollapsed ? (
        <div
          className='text-xl font-bold text-gray-800'
          title={typeof children === 'string' ? children : 'Dashboard'}
        >
          {renderCollapsedContent()}
        </div>
      ) : (
        children
      )}
    </div>
  );
};

export const SidebarContent: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => <nav className='flex-grow p-4 overflow-y-auto'>{children}</nav>;

export const SidebarFooter: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const { isCollapsed } = useSidebar();
  return (
    <div
      className={`p-4 border-t text-gray-800 font-bold ${
        isCollapsed ? 'text-center' : ''
      }`}
    >
      {isCollapsed ? '©' : children}
    </div>
  );
};

export const SidebarLink: React.FC<{
  to: string;
  icon: React.ReactNode;
  children: React.ReactNode;
}> = ({ to, icon, children }) => {
  const { isCollapsed } = useSidebar();
  return (
    <Link
      to={to}
      className={`flex items-center py-2 px-4 text-gray-800 hover:bg-gray-400 rounded transition-colors duration-200 font-medium ${
        isCollapsed ? 'justify-center' : ''
      }`}
    >
      <span className={`${isCollapsed ? 'mr-0' : 'mr-2'}`}>{icon}</span>
      {!isCollapsed && <span>{children}</span>}
    </Link>
  );
};

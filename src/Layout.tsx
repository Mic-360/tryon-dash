import { Home, FileText } from 'lucide-react'
import { SidebarProvider, Sidebar, SidebarHeader, SidebarContent, SidebarFooter, SidebarLink } from './Sidebar'
import { Outlet } from '@tanstack/react-router'

export default function Layout() {
  return (
    <SidebarProvider>
      <div className='flex h-screen bg-gray-100'>
        <Sidebar>
          <SidebarHeader>
            <h1 className='text-xl font-bold text-gray-800'>Dashboard</h1>
          </SidebarHeader>
          <SidebarContent>
            <SidebarLink
              to='/'
              icon={<Home size={18} />}
            >
              Home
            </SidebarLink>
            <SidebarLink
              to='/logs'
              icon={<FileText size={18} />}
            >
              Logs
            </SidebarLink>
          </SidebarContent>
          <SidebarFooter>
            <p className='text-sm text-gray-500'>
              © 2024{' '}
              <a
                href='https://twinverse.in'
                className='text-blue-500 font-medium'
              >
                Twinverse Tech
              </a>
            </p>
          </SidebarFooter>
        </Sidebar>

        {/* Main content */}
        <main className='flex-1 overflow-y-auto p-5'>
          <Outlet />
        </main>
      </div>
    </SidebarProvider>
  );
}
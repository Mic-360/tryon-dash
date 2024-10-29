import {
    createRouter,
    createRoute,
    createRootRoute,
} from '@tanstack/react-router';
import Layout from './Layout';
import LogsPage from './Logs';
import HomePage from './App';

const rootRoute = createRootRoute({
    component: Layout,
});

const homeRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/',
    component: HomePage,
});

const logsRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/logs',
    component: LogsPage,
});

const routeTree = rootRoute.addChildren([homeRoute, logsRoute]);

export const router = createRouter({ routeTree });

declare module '@tanstack/react-router' {
    interface Register {
        router: typeof router;
    }
}
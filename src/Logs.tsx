import { useState, useEffect } from 'react';
import {
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  useReactTable,
  getSortedRowModel,
  SortingState,
  getFilteredRowModel,
  ColumnFiltersState,
} from '@tanstack/react-table';
import { Search, Filter, RefreshCw } from 'lucide-react';

type Log = {
  _id: string;
  personImage: string;
  clothImage: string;
  clothType: string;
  num_inference_steps: number;
  seed: number;
  guidance_scale: number;
  resultImage: string;
  productId: string;
  userId: string;
  businessId: string;
  created_at: string;
};

const columnHelper = createColumnHelper<Log>();

const columns = [
  columnHelper.accessor('businessId', {
    cell: (info) => info.getValue(),
    header: () => <span>Business ID</span>,
  }),
  columnHelper.accessor('clothType', {
    cell: (info) => info.getValue(),
    header: () => <span>Cloth Type</span>,
  }),
  columnHelper.accessor('created_at', {
    cell: (info) => new Date(info.getValue()).toLocaleString(),
    header: () => <span>Timestamp</span>,
  }),
  columnHelper.accessor('num_inference_steps', {
    cell: (info) => info.getValue(),
    header: () => <span>Inference Steps</span>,
  }),
  columnHelper.accessor('seed', {
    cell: (info) => info.getValue(),
    header: () => <span>Seed</span>,
  }),
  columnHelper.accessor('guidance_scale', {
    cell: (info) => info.getValue(),
    header: () => <span>Guidance Scale</span>,
  }),
];

export default function LogsPage() {
  const [logs, setLogs] = useState<Log[]>([]);
  const [sorting, setSorting] = useState<SortingState>([]);
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([]);
  const [error, setError] = useState<string | null>(null);

  const table = useReactTable({
    data: logs,
    columns,
    getCoreRowModel: getCoreRowModel(),
    onSortingChange: setSorting,
    getSortedRowModel: getSortedRowModel(),
    onColumnFiltersChange: setColumnFilters,
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      sorting,
      columnFilters,
    },
  });

  const fetchLogs = async () => {
    try {
      const response = await fetch(
        'http://twinversepc.duckdns.org:8000/api/v1/internal/getAllLogs'
      );
      if (!response.ok) {
        throw new Error('Failed to fetch logs');
      }
      const data: Log[] = await response.json();
      setLogs(data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch logs. Please try again later.');
      console.error('Error fetching logs:', err);
    }
  };

  useEffect(() => {
    fetchLogs(); // Initial fetch

    const intervalId = setInterval(fetchLogs, 5000); // Fetch every 5 seconds

    return () => clearInterval(intervalId); // Clean up on unmount
  }, []);

  return (
    <div className='container mx-auto px-4 py-8'>
      <div className='mb-8'>
        <h1 className='text-3xl font-bold text-gray-800 mb-2'>
          Logs Dashboard
        </h1>
        <p className='text-gray-600'>Real-time log streaming and analysis</p>
      </div>

      {error && (
        <div
          className='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4'
          role='alert'
        >
          <strong className='font-bold'>Error!</strong>
          <span className='block sm:inline'> {error}</span>
        </div>
      )}

      <div className='bg-white shadow-lg rounded-lg overflow-hidden'>
        <div className='p-6 bg-gray-50 border-b border-gray-200'>
          <div className='flex flex-col md:flex-row md:items-center md:justify-between space-y-4 md:space-y-0 md:space-x-4'>
            <div className='flex-1 flex items-center space-x-4'>
              <div className='relative flex-1'>
                <input
                  placeholder='Filter business IDs...'
                  value={
                    (table
                      .getColumn('businessId')
                      ?.getFilterValue() as string) ?? ''
                  }
                  onChange={(event) =>
                    table
                      .getColumn('businessId')
                      ?.setFilterValue(event.target.value)
                  }
                  className='w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                />
                <Search
                  className='absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400'
                  size={18}
                />
              </div>
              <div className='relative'>
                <select
                  value={
                    (table
                      .getColumn('clothType')
                      ?.getFilterValue() as string) ?? ''
                  }
                  onChange={(event) =>
                    table
                      .getColumn('clothType')
                      ?.setFilterValue(event.target.value)
                  }
                  className='appearance-none w-full pl-10 pr-8 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                >
                  <option value=''>All Cloth Types</option>
                  <option value='T-Shirt'>T-Shirt</option>
                  <option value='Jeans'>Jeans</option>
                  <option value='Dress'>Dress</option>
                  <option value='Jacket'>Jacket</option>
                </select>
                <Filter
                  className='absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400'
                  size={18}
                />
              </div>
            </div>
            <button
              onClick={() => setLogs([])}
              className='inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500'
            >
              <RefreshCw
                className='mr-2'
                size={18}
              />
              Clear Logs
            </button>
          </div>
        </div>

        <div className='overflow-x-auto'>
          <table className='min-w-full divide-y divide-gray-200'>
            <thead className='bg-gray-50'>
              {table.getHeaderGroups().map((headerGroup) => (
                <tr key={headerGroup.id}>
                  {headerGroup.headers.map((header) => (
                    <th
                      key={header.id}
                      className='px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider'
                    >
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext()
                          )}
                    </th>
                  ))}
                </tr>
              ))}
            </thead>
            <tbody className='bg-white divide-y divide-gray-200'>
              {table.getRowModel().rows.map((row) => (
                <tr
                  key={row.id}
                  className='hover:bg-gray-50 transition-colors duration-150 ease-in-out'
                >
                  {row.getVisibleCells().map((cell) => (
                    <td
                      key={cell.id}
                      className='px-6 py-4 whitespace-nowrap text-sm text-gray-500'
                    >
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext()
                      )}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {logs.length === 0 && (
          <div className='text-center py-12'>
            <p className='text-gray-500 text-lg'>
              No logs available. New logs will appear here as they are
              generated.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

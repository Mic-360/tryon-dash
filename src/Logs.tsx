import { useState, useEffect } from 'react';
import {
  RefreshCw,
  User,
  Shirt,
  Box,
  Calendar,
  Hash,
  Sliders,
  Zap,
  Image as ImageIcon,
  CheckCircle,
  XCircle,
} from 'lucide-react';

interface Log {
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
}

export default function LogsPage() {
  const [logs, setLogs] = useState<Log[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchLogs = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(
        'http://twinversepc.duckdns.org:8000/api/v1/internal/getAllLogs'
      );
      if (!response.ok) throw new Error('Failed to fetch logs');
      const data: Log[] = await response.json();
      setLogs(data);
    } catch (err) {
      setError('Failed to fetch logs. Please try again later.');
      console.error('Error fetching logs:', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchLogs();
  }, []);

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-GB', {
      day: '2-digit',
      month: 'short',
      year: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  return (
    <div className='container mx-auto px-4 py-8'>
      <div className='flex justify-between items-center mb-8'>
        <div>
          <h1 className='text-3xl font-bold text-gray-800'>Logs Dashboard</h1>
          <p className='text-gray-500 mt-2'>
            Real-time processing logs and analytics
          </p>
        </div>
        <button
          type='button'
          onClick={fetchLogs}
          className='bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg shadow-lg transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 flex items-center'
        >
          <RefreshCw className='mr-2 h-5 w-5' />
          Refresh Logs
        </button>
      </div>

      {isLoading && (
        <div className='text-center py-12'>
          <RefreshCw className='h-8 w-8 animate-spin mx-auto text-blue-500 mb-4' />
          <p className='text-gray-500 text-lg'>Loading logs...</p>
        </div>
      )}

      {error && (
        <div
          className='bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded mb-4'
          role='alert'
        >
          <div className='flex items-center'>
            <XCircle className='h-5 w-5 mr-2' />
            <span>{error}</span>
          </div>
        </div>
      )}

      <div className='space-y-4'>
        {logs.map((log) => (
          <div
            key={log._id}
            className='bg-white rounded-lg shadow-lg overflow-hidden border border-gray-100'
          >
            <div className='px-6 py-4 border-b border-gray-100'>
              <div className='flex items-center justify-between'>
                <div className='flex items-center space-x-4'>
                  <span className='text-lg font-semibold text-gray-800'>
                    Log #{log._id.slice(-6)}
                  </span>
                  <span className='px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800'>
                    {log.clothType}
                  </span>
                </div>
                <div className='flex items-center space-x-2 text-sm text-gray-500'>
                  <Calendar className='h-4 w-4' />
                  <span>{formatDate(log.created_at)}</span>
                </div>
              </div>
            </div>
            <div className='px-6 py-4'>
              <div className='grid grid-cols-1 md:grid-cols-3 gap-6'>
                <div className='space-y-4'>
                  <div className='flex items-center space-x-3 text-gray-700'>
                    <User className='h-5 w-5 text-blue-500' />
                    <div>
                      <p className='text-sm font-medium text-gray-500'>
                        User ID
                      </p>
                      <p className='font-medium'>{log.userId}</p>
                    </div>
                  </div>
                  <div className='flex items-center space-x-3 text-gray-700'>
                    <Box className='h-5 w-5 text-purple-500' />
                    <div>
                      <p className='text-sm font-medium text-gray-500'>
                        Business ID
                      </p>
                      <p className='font-medium'>{log.businessId}</p>
                    </div>
                  </div>
                  <div className='flex items-center space-x-3 text-gray-700'>
                    <Shirt className='h-5 w-5 text-green-500' />
                    <div>
                      <p className='text-sm font-medium text-gray-500'>
                        Product ID
                      </p>
                      <p className='font-medium'>{log.productId}</p>
                    </div>
                  </div>
                </div>
                <div className='space-y-4'>
                  <div className='flex items-center space-x-3 text-gray-700'>
                    <Hash className='h-5 w-5 text-orange-500' />
                    <div>
                      <p className='text-sm font-medium text-gray-500'>
                        Inference Steps
                      </p>
                      <p className='font-medium'>{log.num_inference_steps}</p>
                    </div>
                  </div>
                  <div className='flex items-center space-x-3 text-gray-700'>
                    <Zap className='h-5 w-5 text-yellow-500' />
                    <div>
                      <p className='text-sm font-medium text-gray-500'>Seed</p>
                      <p className='font-medium'>{log.seed}</p>
                    </div>
                  </div>
                  <div className='flex items-center space-x-3 text-gray-700'>
                    <Sliders className='h-5 w-5 text-red-500' />
                    <div>
                      <p className='text-sm font-medium text-gray-500'>
                        Guidance Scale
                      </p>
                      <p className='font-medium'>{log.guidance_scale}</p>
                    </div>
                  </div>
                </div>
                <div className='grid grid-cols-3 gap-4'>
                  <div className='space-y-2'>
                    <p className='text-sm font-medium text-gray-500 flex items-center'>
                      <ImageIcon className='h-4 w-4 mr-1 text-blue-500' />
                      Person
                    </p>
                    <img
                      src={log.personImage}
                      alt='Person'
                      className='w-full h-24 object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200'
                    />
                  </div>
                  <div className='space-y-2'>
                    <p className='text-sm font-medium text-gray-500 flex items-center'>
                      <ImageIcon className='h-4 w-4 mr-1 text-purple-500' />
                      Cloth
                    </p>
                    <img
                      src={log.clothImage}
                      alt='Cloth'
                      className='w-full h-24 object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200'
                    />
                  </div>
                  <div className='space-y-2'>
                    <p className='text-sm font-medium text-gray-500 flex items-center'>
                      <ImageIcon className='h-4 w-4 mr-1 text-green-500' />
                      Result
                    </p>
                    <img
                      src={log.resultImage}
                      alt='Result'
                      className='w-full h-24 object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200'
                    />
                  </div>
                </div>
              </div>
            </div>
            <div className='px-6 py-3 bg-gray-50 border-t border-gray-100'>
              <div className='flex justify-between items-center'>
                <div className='flex items-center space-x-2'>
                  <CheckCircle className='h-4 w-4 text-green-500' />
                  <span className='text-sm text-gray-600'>
                    Processing Complete
                  </span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {!isLoading && logs.length === 0 && (
        <div className='text-center py-12 bg-white rounded-lg shadow-lg'>
          <Box className='h-12 w-12 text-gray-400 mx-auto mb-4' />
          <p className='text-gray-500 text-lg'>No logs available.</p>
          <p className='text-gray-400'>Click refresh to check for new logs.</p>
        </div>
      )}
    </div>
  );
}

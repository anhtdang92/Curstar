'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Box, Button, CircularProgress, FormControl, InputLabel, MenuItem, Select, Typography } from '@mui/material';
import { useDropzone } from 'react-dropzone';
import ReactPlayer from 'react-player';
import { api, Model } from '../services/api';

// Define the structure of the progress data received from WebSocket
interface ProgressData {
  status: 'queued' | 'processing' | 'complete' | 'failed';
  progress?: number;
  current_step?: number;
  total_steps?: number;
  fps?: number;
  eta_seconds?: number;
  error?: string;
}

interface VideoProcessorProps {
  onProcessingComplete?: (resultUrl: string) => void;
}

export const VideoProcessor: React.FC<VideoProcessorProps> = ({ onProcessingComplete }) => {
  const [file, setFile] = useState<File | null>(null);
  const [models, setModels] = useState<Model[]>([]);
  const [selectedModel, setSelectedModel] = useState<string>('');
  const [processing, setProcessing] = useState<boolean>(false);
  const [progress, setProgress] = useState<number>(0);
  const [resultUrl, setResultUrl] = useState<string>('');
  const [currentStep, setCurrentStep] = useState<number | null>(null);
  const [totalSteps, setTotalSteps] = useState<number | null>(null);
  const [fps, setFps] = useState<number | null>(null);
  const [eta, setEta] = useState<number | null>(null);
  const [statusMessage, setStatusMessage] = useState<string>('');
  const [jobId, setJobId] = useState<string | null>(null);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    fetchModels();

    // Cleanup WebSocket on component unmount
    return () => {
      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
        console.log('Closing WebSocket on unmount');
        wsRef.current.close();
      }
    };
  }, []);

  const fetchModels = async () => {
    try {
      const models = await api.getModels();
      setModels(models);
    } catch (error) {
      console.error('Error fetching models:', error);
    }
  };

  const onDrop = (acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
      setResultUrl('');
      setProgress(0);
      setProcessing(false);
      setStatusMessage('');
      setCurrentStep(null);
      setTotalSteps(null);
      setFps(null);
      setEta(null);
      setJobId(null);
      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
         wsRef.current.close();
      }
    }
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'video/*': ['.mp4', '.avi', '.mov']
    },
    multiple: false
  });

  const handleProcess = async () => {
    if (!file || !selectedModel) return;

    // Reset previous state
    setProcessing(true);
    setProgress(0);
    setResultUrl('');
    setStatusMessage('Uploading video...');
    setJobId(null);
    setCurrentStep(null);
    setTotalSteps(null);
    setFps(null);
    setEta(null);

    // Close existing WebSocket connection if any
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      console.log('Closing existing WebSocket connection');
      wsRef.current.close();
    }

    try {
      // 1. Upload file
      const { filename } = await api.uploadVideo(file);
      setStatusMessage('Starting processing...');

      // 2. Start processing job - This now returns a job ID
      const { job_id } = await api.processVideo(filename, selectedModel);
      setJobId(job_id);
      setStatusMessage(`Processing job ${job_id} queued...`);

      // 3. Connect to WebSocket for progress updates using job_id
      console.log(`Connecting to WebSocket for job ID: ${job_id}`);
      const wsUrl = `ws://${window.location.hostname}:8000/ws/${job_id}`;
      console.log(`WebSocket URL: ${wsUrl}`);
      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = () => {
        console.log(`WebSocket connected for job ${job_id}`);
        setStatusMessage('Connected for progress updates...');
      };

      ws.onmessage = (event) => {
        try {
          const data: ProgressData = JSON.parse(event.data);
          console.log('WS Data:', data);

          // Update state based on received data
          setProgress(data.progress ?? progress);
          setCurrentStep(data.current_step ?? currentStep);
          setTotalSteps(data.total_steps ?? totalSteps);
          setFps(data.fps ?? fps);
          setEta(data.eta_seconds ?? eta);

          // Update status message
          switch (data.status) {
            case 'queued':
              setStatusMessage('Job is queued...');
              break;
            case 'processing':
              const progressText = data.progress !== undefined ? `${data.progress}%` : 'Processing...';
              const stepText = currentStep !== null && totalSteps !== null
                ? `(Step ${currentStep}/${totalSteps})` : '';
              setStatusMessage(`Processing ${progressText} ${stepText}`);
              break;
            case 'complete':
              setStatusMessage('Processing complete!');
              setProgress(100);
              setProcessing(false);
              const finalResultUrl = api.getResultUrl(job_id);
              setResultUrl(finalResultUrl);
              if (onProcessingComplete) {
                onProcessingComplete(finalResultUrl);
              }
              ws.close();
              break;
            case 'failed':
              setStatusMessage(`Processing failed: ${data.error || 'Unknown error'}`);
              setProcessing(false);
              setProgress(0);
              ws.close();
              break;
            default:
              setStatusMessage('Receiving unknown update...');
          }
        } catch (e) {
          console.error('Error parsing WebSocket message:', e);
          setStatusMessage('Error receiving progress updates.');
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        setStatusMessage('WebSocket connection error.');
        setProcessing(false);
      };

      ws.onclose = (event) => {
        console.log(`WebSocket closed for job ${job_id}. Code: ${event.code}, Reason: ${event.reason}`);
        if (event.code !== 1000 && event.code !== 1005 && processing) {
             setStatusMessage('WebSocket connection closed unexpectedly.');
             setProcessing(false);
        }
        wsRef.current = null;
      };

    } catch (error: any) {
      console.error('Error processing video:', error);
      setStatusMessage(`Error: ${error.response?.data?.detail || error.message || 'Failed to start processing.'}`);
      setProcessing(false);
    }
  };

  return (
    <Box sx={{ maxWidth: 800, mx: 'auto', p: 3 }}>
      <Box
        {...getRootProps()}
        sx={{
          border: '2px dashed #ccc',
          borderRadius: 2,
          p: 3,
          textAlign: 'center',
          cursor: 'pointer',
          bgcolor: isDragActive ? 'action.hover' : 'background.paper',
          mb: 3
        }}
      >
        <input {...getInputProps()} />
        {file ? (
          <Typography>Selected file: {file.name}</Typography>
        ) : (
          <Typography>Drag and drop a video file here, or click to select</Typography>
        )}
      </Box>

      <FormControl fullWidth sx={{ mb: 3 }} disabled={processing}>
        <InputLabel>Select Model</InputLabel>
        <Select
          value={selectedModel}
          label="Select Model"
          onChange={(e) => setSelectedModel(e.target.value)}
        >
          {models.map((model) => (
            <MenuItem key={model.id} value={model.id}>
              {model.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <Button
        variant="contained"
        onClick={handleProcess}
        disabled={!file || !selectedModel || processing}
        fullWidth
        sx={{ mb: 3 }}
      >
        {processing ? 'Processing...' : 'Process Video'}
      </Button>

      {(processing || statusMessage) && (
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 3, flexDirection: 'column' }}>
          <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
            {processing && <CircularProgress variant={progress > 0 ? "determinate" : "indeterminate"} value={progress} sx={{ mr: 2 }} />}
            <Typography>{statusMessage}</Typography>
          </Box>
          {processing && (
            <Typography variant="body2" color="text.secondary">
              {currentStep !== null && totalSteps !== null && (
                <>Step {currentStep} / {totalSteps} &nbsp;|&nbsp; </>
              )}
              {fps !== null && (
                <>{fps.toFixed(2)} FPS &nbsp;|&nbsp; </>
              )}
              {eta !== null && Number.isFinite(eta) && (
                <>ETA: {Math.round(eta)}s</>
              )}
              {(currentStep === null && fps === null && eta === null) && "Waiting for details..."}
            </Typography>
          )}
        </Box>
      )}

      {resultUrl && (
        <Box sx={{ mt: 3 }}>
          <Typography variant="h6" gutterBottom>
            Processed Video:
          </Typography>
          <Box sx={{ position: 'relative', paddingTop: '56.25%' }}>
            <ReactPlayer
              url={resultUrl}
              controls
              width="100%"
              height="100%"
              style={{ position: 'absolute', top: 0, left: 0 }}
            />
          </Box>
          <Button
            variant="outlined"
            href={resultUrl}
            download
            target="_blank"
            rel="noopener noreferrer"
            sx={{ mt: 2 }}
          >
            Download Processed Video
          </Button>
        </Box>
      )}
    </Box>
  );
}; 
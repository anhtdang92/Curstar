'use client';

import React, { useState, useEffect } from 'react';
import { Box, Button, CircularProgress, FormControl, InputLabel, MenuItem, Select, Typography } from '@mui/material';
import { useDropzone } from 'react-dropzone';
import ReactPlayer from 'react-player';
import { api, Model } from '../services/api';

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

  useEffect(() => {
    fetchModels();
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

    setProcessing(true);
    setProgress(0);

    try {
      // Upload file
      const { filename } = await api.uploadVideo(file);

      // Start processing
      await api.processVideo(filename, selectedModel);

      // Connect to WebSocket for progress updates
      const ws = new WebSocket('ws://localhost:8000/ws');
      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.progress) {
          setProgress(data.progress);
        }
        if (data.status === 'complete') {
          const resultUrl = api.getResultUrl(filename);
          setResultUrl(resultUrl);
          if (onProcessingComplete) {
            onProcessingComplete(resultUrl);
          }
          setProcessing(false);
          ws.close();
        }
      };
    } catch (error) {
      console.error('Error processing video:', error);
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

      <FormControl fullWidth sx={{ mb: 3 }}>
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

      {processing && (
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
          <CircularProgress variant="determinate" value={progress} sx={{ mr: 2 }} />
          <Typography>Processing: {progress}%</Typography>
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
            sx={{ mt: 2 }}
          >
            Download Processed Video
          </Button>
        </Box>
      )}
    </Box>
  );
}; 
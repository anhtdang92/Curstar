import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Box, 
  Typography, 
  Paper, 
  Select, 
  MenuItem, 
  FormControl, 
  InputLabel,
  Button,
  LinearProgress,
  Card,
  CardContent,
  Grid
} from '@mui/material';
import { useDropzone } from 'react-dropzone';
import ReactPlayer from 'react-player';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [models, setModels] = useState({});
  const [selectedModel, setSelectedModel] = useState('');
  const [processing, setProcessing] = useState(false);
  const [progress, setProgress] = useState(0);
  const [result, setResult] = useState(null);

  useEffect(() => {
    // Fetch available models
    axios.get(`${API_URL}/models`)
      .then(response => setModels(response.data.models))
      .catch(error => console.error('Error fetching models:', error));
  }, []);

  const onDrop = async (acceptedFiles) => {
    const file = acceptedFiles[0];
    setFile(file);
    setPreview(URL.createObjectURL(file));
  };

  const { getRootProps, getInputProps } = useDropzone({
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
      const formData = new FormData();
      formData.append('file', file);
      const uploadResponse = await axios.post(`${API_URL}/upload`, formData);
      
      // Start processing
      const processResponse = await axios.post(`${API_URL}/process`, {
        filename: uploadResponse.data.filename,
        model: selectedModel
      });

      // Connect to WebSocket for progress updates
      const ws = new WebSocket(`ws://localhost:8000/ws`);
      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setProgress(data.progress);
        if (data.progress === 100) {
          setResult(`${API_URL}/results/${uploadResponse.data.filename}`);
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
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          STAR Video Processing
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                Upload Video
              </Typography>
              <Box
                {...getRootProps()}
                sx={{
                  border: '2px dashed #ccc',
                  borderRadius: 2,
                  p: 3,
                  textAlign: 'center',
                  cursor: 'pointer',
                  mb: 2
                }}
              >
                <input {...getInputProps()} />
                <Typography>
                  Drag and drop a video file here, or click to select
                </Typography>
              </Box>

              {preview && (
                <Box sx={{ mt: 2 }}>
                  <ReactPlayer
                    url={preview}
                    controls
                    width="100%"
                    height="auto"
                  />
                </Box>
              )}

              <FormControl fullWidth sx={{ mt: 2 }}>
                <InputLabel>Select Model</InputLabel>
                <Select
                  value={selectedModel}
                  onChange={(e) => setSelectedModel(e.target.value)}
                  label="Select Model"
                >
                  {Object.entries(models).map(([key, value]) => (
                    <MenuItem key={key} value={key}>
                      {value}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>

              <Button
                variant="contained"
                fullWidth
                sx={{ mt: 2 }}
                onClick={handleProcess}
                disabled={!file || !selectedModel || processing}
              >
                Process Video
              </Button>
            </Paper>
          </Grid>

          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                Processing Status
              </Typography>
              
              {processing && (
                <Box sx={{ width: '100%', mt: 2 }}>
                  <LinearProgress variant="determinate" value={progress} />
                  <Typography variant="body2" color="text.secondary" align="center" sx={{ mt: 1 }}>
                    {progress}% Complete
                  </Typography>
                </Box>
              )}

              {result && (
                <Card sx={{ mt: 2 }}>
                  <CardContent>
                    <Typography variant="h6" gutterBottom>
                      Processed Video
                    </Typography>
                    <ReactPlayer
                      url={result}
                      controls
                      width="100%"
                      height="auto"
                    />
                    <Button
                      variant="contained"
                      fullWidth
                      sx={{ mt: 2 }}
                      href={result}
                      download
                    >
                      Download Result
                    </Button>
                  </CardContent>
                </Card>
              )}
            </Paper>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}

export default App; 
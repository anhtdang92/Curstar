'use client';

import { Container, Typography, Box } from '@mui/material';
import { VideoProcessor } from './components/VideoProcessor';

export default function Home() {
  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          STAR Video Processing
        </Typography>
        <Typography variant="h6" component="h2" gutterBottom align="center" color="text.secondary">
          Upload your video and select a model to process it
        </Typography>
        <VideoProcessor />
      </Box>
    </Container>
  );
} 
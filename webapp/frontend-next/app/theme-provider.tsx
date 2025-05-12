'use client';
import * as React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import NextAppDirEmotionCacheProvider from './EmotionCache';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#00e0ff', // Futuristic blue/cyan
    },
    secondary: {
      main: '#ff2d55', // Apple accent pink
    },
    background: {
      default: '#181a1b', // Deep dark
      paper: 'rgba(30,32,34,0.85)', // Glassy effect
    },
    text: {
      primary: '#f5f6fa',
      secondary: '#b0b3b8',
    },
  },
  typography: {
    fontFamily: [
      'SF Pro Display',
      'Segoe UI',
      'Roboto',
      'Helvetica Neue',
      'Arial',
      'sans-serif',
    ].join(','),
    h1: { fontWeight: 700, letterSpacing: '-1.5px' },
    h2: { fontWeight: 700, letterSpacing: '-1px' },
    h3: { fontWeight: 600 },
    h4: { fontWeight: 600 },
    h5: { fontWeight: 500 },
    h6: { fontWeight: 500 },
    button: { textTransform: 'none', fontWeight: 600 },
  },
  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          backdropFilter: 'blur(12px)',
          backgroundImage: 'none',
          borderRadius: 16,
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          fontWeight: 600,
          letterSpacing: '0.5px',
        },
      },
    },
    MuiContainer: {
      styleOverrides: {
        root: {
          paddingTop: '32px',
          paddingBottom: '32px',
        },
      },
    },
  },
});

export default function MuiThemeProvider({ children }: { children: React.ReactNode }) {
  return (
    <NextAppDirEmotionCacheProvider options={{ key: 'mui' }}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        {children}
      </ThemeProvider>
    </NextAppDirEmotionCacheProvider>
  );
} 
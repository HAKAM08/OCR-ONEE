import React from "react";
import ReactDOM from "react-dom/client";

import { QueryClient } from "@tanstack/react-query";
import { QueryClientProvider } from "@tanstack/react-query";

import { BrowserRouter } from "react-router-dom";

import { Toaster } from "react-hot-toast";

import App from "./App";

import "./index.css";

import { AuthProvider } from "@/contexts/AuthContext";
import { pdfjs } from "react-pdf";
import "react-pdf/dist/Page/AnnotationLayer.css";
import "react-pdf/dist/Page/TextLayer.css";

const queryClient = new QueryClient();
pdfjs.GlobalWorkerOptions.workerSrc =
  `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;
ReactDOM.createRoot(
  document.getElementById("root")!
).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <AuthProvider>
          <App />
          <Toaster position="top-right" />
        </AuthProvider>
      </BrowserRouter>
    </QueryClientProvider>
  </React.StrictMode>
);
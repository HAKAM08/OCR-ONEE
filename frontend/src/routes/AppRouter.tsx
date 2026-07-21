import { Routes, Route } from "react-router-dom";

import ProtectedRoute from "./ProtectedRoute";

import DashboardLayout from "@/layouts/DashboardLayout";

import Login from "@/pages/Login";
import Dashboard from "@/pages/Dashboard";
import Upload from "@/pages/Upload";
import Search from "@/pages/Search";
import Documents from "@/pages/Documents";
import Viewer from "@/pages/Viewer";

export default function AppRouter() {
  return (
    <Routes>

      <Route
        path="/login"
        element={<Login />}
      />

      <Route element={<ProtectedRoute />}>

        <Route element={<DashboardLayout />}>

          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/upload"
            element={<Upload />}
          />

          <Route
            path="/documents"
            element={<Documents />}
          />

          <Route
            path="/search"
            element={<Search />}
          />

          <Route
            path="/viewer/:id"
            element={<Viewer />}
          />

        </Route>

      </Route>

    </Routes>
  );
}
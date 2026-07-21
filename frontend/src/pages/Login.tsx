import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import toast from "react-hot-toast";

import { AuthAPI } from "@/api/auth";
import { useAuth } from "@/contexts/AuthContext";

import type { LoginRequest } from "@/types/auth";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function Login() {
  const navigate = useNavigate();

  const { login } = useAuth();

  const [loading, setLoading] = useState(false);

  const {
    register,
    handleSubmit,
  } = useForm<LoginRequest>();

  async function onSubmit(data: LoginRequest) {
    try {
      setLoading(true);

      const response = await AuthAPI.login(data);

      login(response.access_token);

      toast.success("Login successful.");

      navigate("/");

    } catch (error) {

      toast.error("Invalid email or password.");

      console.error(error);

    } finally {

      setLoading(false);

    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-100">

      <div className="w-full max-w-md rounded-xl bg-white p-8 shadow-xl">

        <h1 className="mb-2 text-center text-3xl font-bold">
          ONEE OCR
        </h1>

        <p className="mb-8 text-center text-slate-500">
          Intelligent Document Management System
        </p>

        <form
          onSubmit={handleSubmit(onSubmit)}
          className="space-y-5"
        >

          <div>

            <Label>Email</Label>

            <Input

              type="email"

              placeholder="example@email.com"

              {...register("email", {
                required: true,
              })}

            />

          </div>

          <div>

            <Label>Password</Label>

            <Input

              type="password"

              placeholder="********"

              {...register("password", {
                required: true,
              })}

            />

          </div>

          <Button
            className="w-full"
            disabled={loading}
          >

            {loading
              ? "Signing in..."
              : "Login"}

          </Button>

        </form>

      </div>

    </div>
  );
}
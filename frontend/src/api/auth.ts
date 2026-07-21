import api from "@/api/axios";

import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
} from "@/types/auth";

import type { User } from "@/types/user";

export const AuthAPI = {
  async login(data: LoginRequest): Promise<LoginResponse> {
    const response = await api.post<LoginResponse>(
      "/auth/login",
      data
    );

    return response.data;
  },

  async register(data: RegisterRequest): Promise<User> {
    const response = await api.post<User>(
      "/auth/register",
      data
    );

    return response.data;
  },
};
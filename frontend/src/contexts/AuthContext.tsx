import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

import { jwtDecode } from "jwt-decode";

interface JwtPayload {
  sub: string;
  role: string;
  exp: number;
}

interface AuthContextType {
  token: string | null;
  user: JwtPayload | null;
  login: (token: string) => void;
  logout: () => void;
  isAuthenticated: boolean;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType>(
  {} as AuthContextType
);

export function AuthProvider({
  children,
}: {
  children: React.ReactNode;
}) {

  const [token, setToken] = useState<string | null>(null);

  const [user, setUser] =
    useState<JwtPayload | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const stored = localStorage.getItem("token");

    if (stored) {
      setToken(stored);
      setUser(jwtDecode(stored));
    }

    setLoading(false);

  }, []);

  function login(jwt: string) {

    localStorage.setItem("token", jwt);

    setToken(jwt);

    setUser(jwtDecode(jwt));

  }

  function logout() {

    localStorage.removeItem("token");

    setToken(null);

    setUser(null);

  }

  return (

    <AuthContext.Provider
      value={{
        token,
        user,
        login,
        logout,
        isAuthenticated: !!token,
        loading,
      }}
    >

      {children}

    </AuthContext.Provider>

  );

}

export function useAuth() {
  return useContext(AuthContext);
}
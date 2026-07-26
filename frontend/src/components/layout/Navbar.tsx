import { Bell, Search } from "lucide-react";

import { Avatar, AvatarFallback } from "@/components/ui/avatar";

import { useAuth } from "@/contexts/AuthContext";

export default function Navbar() {
  const { user } = useAuth();

  const initials =
    user?.sub
      ?.split("@")[0]
      .substring(0, 2)
      .toUpperCase() ?? "US";

  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-8">

      <div className="flex items-center gap-4">

        <h2 className="text-2xl font-semibold text-slate-800">
          Welcome, {user?.sub}
        </h2>

      </div>

      <div className="flex items-center gap-6">

        



        <div className="flex items-center gap-3">

          <Avatar>

            <AvatarFallback>

              {initials}

            </AvatarFallback>

          </Avatar>

          <div>

            <p className="text-sm font-semibold">

              {user?.sub}

            </p>

            <p className="text-xs text-slate-500">

              {user?.role}

            </p>

          </div>

        </div>

      </div>

    </header>
  );
}
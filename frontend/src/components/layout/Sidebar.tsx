import { NavLink } from "react-router-dom";
import { LogOut } from "lucide-react";

import { navigation } from "@/utils/navigation";
import { useAuth } from "@/contexts/AuthContext";

export default function Sidebar() {
  const { logout } = useAuth();

  return (
    <aside className="flex h-screen w-72 flex-col border-r bg-white">

      <div className="border-b p-6">

        <h1 className="text-2xl font-bold text-slate-900">
          ONEE OCR
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Intelligent Document Management
        </p>

      </div>

      <nav className="flex-1 space-y-2 p-4">

        {navigation.map((item) => {

          const Icon = item.icon;

          return (

            <NavLink
              key={item.href}
              to={item.href}
              className={({ isActive }) =>
                `flex items-center gap-3 rounded-lg px-4 py-3 transition-all ${
                  isActive
                    ? "bg-blue-600 text-white"
                    : "text-slate-700 hover:bg-slate-100"
                }`
              }
            >

              <Icon size={20} />

              <span>{item.title}</span>

            </NavLink>

          );

        })}

      </nav>

      <div className="border-t p-4">

        <button
          onClick={logout}
          className="flex w-full items-center gap-3 rounded-lg px-4 py-3 text-red-600 transition hover:bg-red-50"
        >

          <LogOut size={20} />

          Logout

        </button>

      </div>

    </aside>
  );
}
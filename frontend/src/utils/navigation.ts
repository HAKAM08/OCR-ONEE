import {
  LayoutDashboard,
  Upload,
  FileText,
  Search,
  Settings,
} from "lucide-react";

export interface NavigationItem {
  title: string;
  href: string;
  icon: React.ElementType;
}

export const navigation: NavigationItem[] = [
  {
    title: "Dashboard",
    href: "/",
    icon: LayoutDashboard,
  },
  {
    title: "Upload",
    href: "/upload",
    icon: Upload,
  },
  {
    title: "Documents",
    href: "/documents",
    icon: FileText,
  },
  {
    title: "Search",
    href: "/search",
    icon: Search,
  },
  {
    title: "Settings",
    href: "/settings",
    icon: Settings,
  },
];
import { useQuery } from "@tanstack/react-query";

import {
    DashboardAPI
} from "@/api/dashboard";

export function useDashboard() {

    return useQuery({

        queryKey: ["dashboard"],

        queryFn: DashboardAPI.getStats,

        staleTime: 30000

    });

}
import { useQuery } from "@tanstack/react-query";

import { SearchAPI } from "@/api/search";

export function useSearch(query: string) {

    return useQuery({

        queryKey: ["search", query],

        queryFn: () => SearchAPI.search(query),

        enabled: query.length >= 2,

    });

}
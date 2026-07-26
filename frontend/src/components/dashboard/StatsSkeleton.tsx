import { Skeleton } from "@/components/ui/skeleton";

export default function StatsSkeleton() {
    return (
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

            {[1,2,3,4].map((item) => (

                <div
                    key={item}
                    className="rounded-xl border bg-white p-6 space-y-4"
                >

                    <Skeleton className="h-4 w-24" />

                    <Skeleton className="h-10 w-20" />

                    <Skeleton className="h-12 w-12 rounded-xl" />

                </div>

            ))}

        </div>
    );
}
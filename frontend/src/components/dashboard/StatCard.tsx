import { LucideIcon } from "lucide-react";

import { Card } from "@/components/ui/card";

interface StatCardProps {

    title: string;

    value: number | string;

    icon: LucideIcon;

    color: string;

}

export default function StatCard({

    title,

    value,

    icon: Icon,

    color,

}: StatCardProps) {

    return (

        <Card className="transition-all duration-300 hover:shadow-xl hover:-translate-y-1">

            <div className="flex items-center justify-between p-6">

                <div>

                    <p className="text-sm text-slate-500">

                        {title}

                    </p>

                    <h2 className="mt-2 text-4xl font-bold">

                        {value}

                    </h2>

                </div>

                <div
                    className={`flex h-14 w-14 items-center justify-center rounded-xl ${color}`}
                >

                    <Icon
                        className="text-white"
                        size={28}
                    />

                </div>

            </div>

        </Card>

    );

}
import {
    CheckCircle2,
    Database,
    ScanText,
    Search,
} from "lucide-react";

import { Card } from "@/components/ui/card";

export default function SystemStatus() {

    const services = [

        {
            name: "PostgreSQL",
            icon: Database,
            color: "text-green-600",
        },

        {
            name: "OCR Engine",
            icon: ScanText,
            color: "text-green-600",
        },

        {
            name: "Elasticsearch",
            icon: Search,
            color: "text-green-600",
        },

    ];

    return (

        <Card className="p-6">

            <h2 className="mb-6 text-xl font-semibold">

                System Status

            </h2>

            <div className="space-y-5">

                {services.map((service) => {

                    const Icon = service.icon;

                    return (

                        <div
                            key={service.name}
                            className="flex items-center justify-between"
                        >

                            <div className="flex items-center gap-3">

                                <Icon
                                    className={service.color}
                                    size={20}
                                />

                                <span>

                                    {service.name}

                                </span>

                            </div>

                            <CheckCircle2
                                className="text-green-600"
                                size={20}
                            />

                        </div>

                    );

                })}

            </div>

        </Card>

    );

}
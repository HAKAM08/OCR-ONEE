import { Search } from "lucide-react";

interface Props {

    value: string;

    onChange: (value: string) => void;

}

export default function DocumentsToolbar({

    value,

    onChange,

}: Props) {

    return (

        <div className="flex items-center gap-4">

            <div className="relative w-full max-w-md">

                <Search
                    className="absolute left-3 top-3 text-slate-400"
                    size={18}
                />

                <input
                    value={value}
                    onChange={(e) => onChange(e.target.value)}
                    placeholder="Search documents..."
                    className="w-full rounded-lg border py-2 pl-10 pr-4"
                />

            </div>

        </div>

    );

}
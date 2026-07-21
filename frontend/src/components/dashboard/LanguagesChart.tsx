import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Tooltip,
} from "recharts";

interface Props {
  data: {
    name: string;
    value: number;
  }[];
}

export default function LanguagesChart({
  data,
}: Props) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-lg font-semibold">
        Languages
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <PieChart>

          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={100}
          />

          <Tooltip />

        </PieChart>

      </ResponsiveContainer>

    </div>
  );
}
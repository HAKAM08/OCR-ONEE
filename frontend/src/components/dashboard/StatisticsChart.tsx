import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

interface Props {
  data: {
    name: string;
    value: number;
  }[];
}

export default function StatisticsChart({
  data,
}: Props) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-sm">

      <h2 className="mb-6 text-lg font-semibold">
        Upload Statistics
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={data}>

          <XAxis dataKey="name" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="value" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
}
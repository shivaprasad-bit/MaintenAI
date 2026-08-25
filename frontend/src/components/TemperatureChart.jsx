import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

export default function TemperatureChart({ data }) {
  return (
    <div className="bg-[#081527] border border-cyan-500/20 rounded-2xl p-5 shadow-lg shadow-cyan-500/10 h-[320px]">
      <h2 className="text-lg font-semibold text-cyan-300 mb-4">
        Live Temperature Trend
      </h2>

      <ResponsiveContainer width="100%" height="90%">
        <LineChart data={data}>
          <CartesianGrid stroke="#1e293b" strokeDasharray="3 3" />

          <XAxis
            dataKey="timestamp"
            stroke="#64748b"
          />

          <YAxis
            stroke="#64748b"
            domain={[35,95]}
          />

          <Tooltip/>

          <Line
            type="monotone"
            dataKey="temperature"
            stroke="#22d3ee"
            strokeWidth={3}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
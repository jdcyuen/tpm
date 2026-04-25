import PortfolioGrid from "@/components/PortfolioGrid";

export default function Home() {
  const data = [
    {
      account_number: "250464524",
      account_name: "Rollover IRA",
      ticker: "AAPL",
      description: "Apple Inc",
      last_price: 180,
      price_change: 1.2,
      daily_gain: 120,
      daily_gain_pct: 0.7,
      total_gain: 2000,
      total_gain_pct: 12,
      market_value: 15000,
      percent_of_account: 10,
      quantity: 80,
      avg_cost: 150,
      cost_basis_total: 12000,
      week_52_range: "140 - 200"
    },
    {
      account_number: "250464524",
      account_name: "Rollover IRA",
      ticker: "NVDA",
      description: "Nvidia Inc",
      last_price: 900,
      price_change: -10,
      daily_gain: -500,
      daily_gain_pct: -1.2,
      total_gain: 5000,
      total_gain_pct: 25,
      market_value: 20000,
      percent_of_account: 15,
      quantity: 22,
      avg_cost: 600,
      cost_basis_total: 13200,
      week_52_range: "400 - 1000"
    }
  ];

  return (
    <main style={{ padding: "20px" }}>
      <h1>Total Portfolio Manager</h1>
      <PortfolioGrid rowData={data} />
    </main>
  );
}
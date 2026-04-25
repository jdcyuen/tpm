"use client";

import { AgGridReact } from "ag-grid-react";
import { themeQuartz, ModuleRegistry, AllCommunityModule } from "ag-grid-community";

ModuleRegistry.registerModules([AllCommunityModule]);

const PortfolioGrid = ({ rowData }: { rowData: any[] }) => {

    const columnDefs = [
        {
            field: "account_number",
            headerName: "Account Number",
            pinned: "left",
            width: 120,
            cellStyle: { fontFamily: "monospace", color: "#6b7280" }
        },
        {
            field: "account_name",
            headerName: "Account Name",
            pinned: "left",
            width: 120,
            cellStyle: { fontWeight: "600" }
        },
        {
            field: "ticker",
            headerName: "Ticker",
            pinned: "left",
            width: 100,
            cellStyle: { fontWeight: "600", color: "#111827" }
        },

        {
            field: "description",
            headerName: "Description",
            minWidth: 130
        },

        {
            field: "quantity",
            headerName: "Qty",
            minWidth: 70,
            cellStyle: { textAlign: "right" }
        },


        {
            field: "last_price",
            headerName: "Last Price",
            minWidth: 100,
            valueFormatter: (p: any) => `$${p.value?.toFixed(2)}`,
            cellStyle: { textAlign: "right" }
        },

        {
            field: "price_change",
            headerName: "Last Price Chg",
            minWidth: 130,
            valueFormatter: (p: any) => `${p.value?.toFixed(2)}`,
            cellStyle: (p: any) => ({
                textAlign: "right",
                color: p.value >= 0 ? "#16a34a" : "#dc2626"
            })
        },

        {
            field: "market_value",
            headerName: "Current Value",
            minWidth: 130,
            valueFormatter: (p: any) => `$${p.value?.toLocaleString()}`,
            cellStyle: { textAlign: "right" }
        },

        {
            field: "daily_gain",
            headerName: "Today's Gain/Loss Dollar",
            valueFormatter: (p: any) => `$${p.value?.toFixed(2)}`,
            minWidth: 130,
            cellStyle: (p: any) => ({
                textAlign: "right",
                color: p.value >= 0 ? "#16a34a" : "#dc2626"
            })
        },

        {
            field: "daily_gain_pct",
            headerName: "Today's Gain/Loss Percent",
            minWidth: 130,
            valueFormatter: (p: any) => `${p.value?.toFixed(2)}%`,
            cellStyle: (p: any) => ({
                textAlign: "right",
                color: p.value >= 0 ? "#16a34a" : "#dc2626"
            })
        },

        {
            field: "total_gain",
            headerName: "Total Gain/Loss Dollar",
            minWidth: 130,
            valueFormatter: (p: any) => `$${p.value?.toFixed(2)}`,
            cellStyle: (p: any) => ({
                textAlign: "right",
                color: p.value >= 0 ? "#16a34a" : "#dc2626"
            })
        },

        {
            field: "total_gain_pct",
            headerName: "Total Gain/Loss Percent",
            minWidth: 130,
            valueFormatter: (p: any) => `${p.value?.toFixed(2)}%`,
            cellStyle: (p: any) => ({
                textAlign: "right",
                color: p.value >= 0 ? "#16a34a" : "#dc2626"
            })
        },

        {
            field: "percent_of_account",
            headerName: "% of Account",
            minWidth: 130,
            valueFormatter: (p: any) => `${p.value?.toFixed(2)}%`,
            cellStyle: { textAlign: "right" }
        },

        {
            field: "cost_basis_total",
            headerName: "Cost Basis Total",
            minWidth: 130,
            valueFormatter: (p: any) => `$${p.value?.toLocaleString()}`,
            cellStyle: { textAlign: "right" }
        },

        {
            field: "avg_cost",
            headerName: "Avg Cost Basis",
            minWidth: 130,
            valueFormatter: (p: any) => `$${p.value?.toFixed(2)}`,
            cellStyle: { textAlign: "right" }
        },

        {
            field: "week_52_range",
            headerName: "52 Week Range",
            minWidth: 120,
            cellStyle: { textAlign: "center" }
        }
    ];

    const defaultColDef = {
        resizable: true,
        sortable: true,
        filter: true,

        flex: 1,

        wrapHeaderText: true,     // ✅ enables wrapping
        autoHeaderHeight: true    // ✅ lets header grow vertically
    };

    return (
        <div style={{ height: 600, width: "100%" }}>
            <AgGridReact
                theme={themeQuartz}
                rowData={rowData}
                columnDefs={columnDefs}
                defaultColDef={defaultColDef}
            />
        </div>
    );
};

export default PortfolioGrid;
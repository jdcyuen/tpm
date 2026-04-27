-- Ensure schema exists
CREATE SCHEMA IF NOT EXISTS tpm;

---------------------------------------------------
-- 1. CORE TABLES (no dependencies)
---------------------------------------------------

CREATE TABLE IF NOT EXISTS tpm.accounts (
    id SERIAL PRIMARY KEY,
    account_number VARCHAR(50) NOT NULL,
    account_name VARCHAR(100),
    provider VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS tpm.securities (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(20) NOT NULL UNIQUE,
    description VARCHAR(255),
    asset_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS tpm.snapshots (
    id SERIAL PRIMARY KEY,
    snapshot_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

---------------------------------------------------
-- 2. DEPENDENT TABLE
---------------------------------------------------

CREATE TABLE IF NOT EXISTS tpm.positions (
    id SERIAL PRIMARY KEY,

    account_id INT,
    security_id INT,
    snapshot_id INT,

    quantity NUMERIC(20,6),
    avg_cost NUMERIC(20,6),
    cost_basis_total NUMERIC(20,2),
    market_value NUMERIC(20,2),
    percent_of_account NUMERIC(10,4),

    daily_gain NUMERIC(20,2),
    daily_gain_pct NUMERIC(10,4),
    total_gain NUMERIC(20,2),
    total_gain_pct NUMERIC(10,4),

    created_at TIMESTAMP DEFAULT NOW()
);

---------------------------------------------------
-- 3. PRICES TABLE
---------------------------------------------------

CREATE TABLE IF NOT EXISTS tpm.prices (
    id SERIAL PRIMARY KEY,

    security_id INT,
    price_date DATE NOT NULL,

    last_price NUMERIC(20,6),
    price_change NUMERIC(20,6),
    week_52_low NUMERIC(20,6),
    week_52_high NUMERIC(20,6),

    UNIQUE (security_id, price_date)
);

---------------------------------------------------
-- 4. FOREIGN KEYS (added AFTER tables exist)
---------------------------------------------------

ALTER TABLE tpm.positions
ADD CONSTRAINT fk_positions_account
FOREIGN KEY (account_id) REFERENCES tpm.accounts(id);

ALTER TABLE tpm.positions
ADD CONSTRAINT fk_positions_security
FOREIGN KEY (security_id) REFERENCES tpm.securities(id);

ALTER TABLE tpm.positions
ADD CONSTRAINT fk_positions_snapshot
FOREIGN KEY (snapshot_id) REFERENCES tpm.snapshots(id);

ALTER TABLE tpm.prices
ADD CONSTRAINT fk_prices_security
FOREIGN KEY (security_id) REFERENCES tpm.securities(id);
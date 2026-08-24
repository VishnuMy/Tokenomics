from dataclasses import dataclass


@dataclass(slots=True)
class EconomicsInput:
    transactions_per_month: int
    minutes_per_transaction: float
    loaded_hourly_cost: float
    success_rate: float
    human_review_rate: float
    monthly_inference_cost: float
    monthly_platform_cost: float
    implementation_cost: float
    retry_rate: float = 0.0
    avg_cost_per_attempt: float = 0.0


def calculate(x: EconomicsInput) -> dict[str, float | None]:
    current = (
        x.transactions_per_month
        * 12
        * x.minutes_per_transaction
        / 60
        * x.loaded_hourly_cost
    )
    realized_automation = x.success_rate * (1 - x.human_review_rate)
    labor_benefit = current * realized_automation
    retry_tax = (
        x.transactions_per_month
        * 12
        * x.retry_rate
        * x.avg_cost_per_attempt
    )
    run_cost = 12 * (x.monthly_inference_cost + x.monthly_platform_cost) + retry_tax
    net = labor_benefit - run_cost
    payback = None if net <= 0 else x.implementation_cost / net * 12

    return {
        "current_cost": round(current, 2),
        "labor_benefit": round(labor_benefit, 2),
        "retry_tax": round(retry_tax, 2),
        "annual_run_cost": round(run_cost, 2),
        "net_annual_value": round(net, 2),
        "payback_months": None if payback is None else round(payback, 1),
    }


if __name__ == "__main__":
    example = EconomicsInput(
        transactions_per_month=25_000,
        minutes_per_transaction=6,
        loaded_hourly_cost=60,
        success_rate=0.90,
        human_review_rate=0.12,
        monthly_inference_cost=12_000,
        monthly_platform_cost=8_000,
        implementation_cost=350_000,
        retry_rate=0.10,
        avg_cost_per_attempt=0.04,
    )
    print(calculate(example))

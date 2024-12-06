import Entity
import EntityPortfolio

portfolio = EntityPortfolio.EntityPortfolio()

def test_add_asset():
    new_asset = Entity.Entity(49.2, 4, "test asset", "test desc", False, "n/a")
    portfolio.add_asset(new_asset)
    assert new_asset == portfolio.get_entity(new_asset.get_entity_id())

def test_add_liability():
    new_liability = Entity.Entity(10.2, 4, "test liability", "test dec", False, "n/a")
    portfolio.add_liability(new_liability)
    assert new_liability == portfolio.get_entity(new_liability.get_entity_id())


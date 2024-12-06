import Entity
import EntityPortfolio

portfolio = EntityPortfolio.EntityPortfolio()

def test_delete_asset():
    new_asset = Entity.Entity(49.2, 4, "test asset", "test desc", False, "n/a")
    portfolio.add_asset(new_asset)
    assert portfolio.entity_count == 1
    portfolio.remove_asset(new_asset.get_entity_id())
    assert portfolio.entity_count == 0
    assert portfolio.assets == []

def test_delete_liability():
    new_liability = Entity.Entity(10.2, 4, "test liability", "test dec", False, "n/a")
    portfolio.add_liability(new_liability)
    assert portfolio.entity_count == 1
    portfolio.remove_liability(new_liability.get_entity_id())
    assert portfolio.entity_count == 0    
    assert portfolio.liabilities == []
    

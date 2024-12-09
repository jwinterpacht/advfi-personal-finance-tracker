import Entity
import EntityPortfolio

portfolio = EntityPortfolio.EntityPortfolio()

#testing add entity

def test_add_asset():
    new_asset = Entity.Entity(49.2, 4, "test asset", "test desc", False, "n/a")
    portfolio.add_asset(new_asset, False)
    assert new_asset == portfolio.get_entity(new_asset.get_entity_id())

def test_add_liability():
    new_liability = Entity.Entity(10.2, 4, "test liability", "test desc", False, "n/a")
    portfolio.add_liability(new_liability, False)
    assert new_liability == portfolio.get_entity(new_liability.get_entity_id())

#testing edit entity
def test_edit_asset():
    new_asset = portfolio.get_entity(1)
    assert new_asset.get_single_value() == 49.2
    assert new_asset.get_amount() == 4
    assert new_asset.get_total_value() == 196.8 #49.2 * 4
    assert new_asset.get_name() == "test asset"
    assert new_asset.get_description() == "test desc"
    assert new_asset.get_auto_update() == False

    new_asset.set_amount(2)
    new_asset.set_single_value(10)
    new_asset.set_name("test asset 2")
    new_asset.set_description("test desc 2")

    assert new_asset.get_single_value() == 10
    assert new_asset.get_amount() == 2
    assert new_asset.get_total_value() == 20
    assert new_asset.get_name() == "test asset 2"
    assert new_asset.get_description() == "test desc 2"
    
    

def test_edit_liability():
    new_liability = portfolio.get_entity(2)
    assert new_liability.get_single_value() == 10.2
    assert new_liability.get_amount() == 4
    assert new_liability.get_total_value() == 40.8 #49.2 * 4
    assert new_liability.get_name() == "test liability"
    assert new_liability.get_description() == "test desc"
    assert new_liability.get_auto_update() == False

    new_liability.set_amount(2)
    new_liability.set_single_value(10)
    new_liability.set_name("test liability 2")
    new_liability.set_description("test desc 2")

    assert new_liability.get_single_value() == 10
    assert new_liability.get_amount() == 2
    assert new_liability.get_total_value() == 20
    assert new_liability.get_name() == "test liability 2"
    assert new_liability.get_description() == "test desc 2"

#testing remove entity
def test_delete_asset():
    new_asset = portfolio.get_entity(1)
    assert portfolio.entity_count == 2
    portfolio.remove_asset(new_asset.get_entity_id())
    assert portfolio.entity_count == 1
    assert portfolio.assets == []

def test_delete_liability():
    new_liability = portfolio.get_entity(2)
    assert portfolio.entity_count == 1
    portfolio.remove_liability(new_liability.get_entity_id())
    assert portfolio.entity_count == 0    
    assert portfolio.liabilities == []
    

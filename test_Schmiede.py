def test_schneiden():
    from Schmiede import Schmiede, Piller

    s=Schmiede()
    p=s.schneiden()

    assert isinstance(p, Piller)

def test_erhitzen():
    from Schmiede import Schmiede, Piller

    s=Schmiede()
    p=Piller()
    s.erhitzen(p)

    assert isinstance(p, Piller)
    assert p.erhitzt

def test_biegen():
    from Schmiede import Schmiede, Piller

    s=Schmiede()
    p=Piller()
    p.erhitzt = True

    s.biegen(p)

    assert isinstance(p, Piller)
    assert p.gebogen

def test_schmieden():
    from Schmiede import Schmiede, Piller
    from Zange import Zange

    s=Schmiede()
    p=Piller()

    p.erhitzt = True
    p.gebogen = True

    z = s.schmieden(p)

    assert isinstance(z, Zange)
    assert z.geschmiedet

def test_abgraten():
    from Schmiede import Schmiede, Piller
    from Zange import Zange

    s=Schmiede()
    z=Zange()

    z.erhitzt = True
    z.gebogen = True
    z.geschmiedet = True

    s.abgraten(z)

    assert isinstance(z, Zange)
    assert z.abgegratet

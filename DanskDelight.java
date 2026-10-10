package dk.danskdelight;

import dk.danskdelight.registry.ModCreativeTabs;
import dk.danskdelight.registry.ModItems;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

/**
 * Dansk Delight - traditionel dansk mad som tilføjelse til Farmer's Delight.
 */
@Mod(DanskDelight.MOD_ID)
public class DanskDelight {
    public static final String MOD_ID = "danskdelight";

    public DanskDelight() {
        IEventBus modBus = FMLJavaModLoadingContext.get().getModEventBus();
        ModItems.ITEMS.register(modBus);
        ModCreativeTabs.TABS.register(modBus);
    }
}
